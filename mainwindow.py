from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui_mainwindow import Ui_MainWindow

from energy_systems import pipe_sizing as ps
from pyXSteam.XSteam import XSteam
import sigfig as sf
import pandas as pd
import math

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.button_add_row.clicked.connect(self.add_row)
        self.button_remove_row.clicked.connect(self.delete_row)
        self.button_reset_rows.clicked.connect(self.reset_rows)

        self.button_pipe_calculate.clicked.connect(self.pipe_calculate)

        self.button_pipe_excel.clicked.connect(self.pipe_to_excel)
        self.button_wall_autofill.clicked.connect(self.wall_autofill)
        self.button_wall_calculate.clicked.connect(self.wall_calculate)
        self.button_wall_excel.clicked.connect(self.wall_to_excel)
        self.line_edit_design_temperature.textChanged.connect(self.update_fahrenheit)
        self.line_edit_SE_ksi.textChanged.connect(self.update_SE)

        #Pump
        self.button_get_capacity.clicked.connect(self.update_capacity)
        self.button_hydraulics.clicked.connect(self.calculate_hydraulics)

    def add_row(self):
        row_count = self.table_fittings.rowCount()
        selected_row = self.table_fittings.currentRow()

        if selected_row == -1:
            self.table_fittings.insertRow(row_count)
        else:
            self.table_fittings.insertRow(selected_row + 1)

    def delete_row(self):
        row_count = self.table_fittings.rowCount()
        selected_row = self.table_fittings.currentRow()
        if row_count > 1:
            if selected_row == -1:
                self.table_fittings.removeRow(row_count-1)  
            else:
                self.table_fittings.removeRow(selected_row)
        else:
            self.table_fittings.clearContents()

    def reset_rows(self):
        for i in range(1, self.table_fittings.rowCount()):
            self.table_fittings.removeRow(0)
        self.table_fittings.clearContents()

    def pipe_calculate(self):
        #Calculate Fittings
        try:
            names = []
            resistances = []
            quantities = []
            sum_resistances = []

            x = self.table_fittings.rowCount()
            if self.table_fittings.columnCount() < 4:
                sum_label = QTableWidgetItem("nL/D")
                self.table_fittings.insertColumn(3)
                self.table_fittings.setHorizontalHeaderItem(3, sum_label)

            for i in range(x):
                    names.append(self.table_fittings.item(i, 0).text())
                    resistance = float(self.table_fittings.item(i, 1).text())
                    quantity = float(self.table_fittings.item(i, 2).text())
                    sum_resistance = QTableWidgetItem(str(resistance*quantity))
                    self.table_fittings.setItem(i, 3, sum_resistance)
                    resistances.append(resistance)
                    quantities.append(quantity)
                    sum_resistances.append(resistance * quantity)
            
            total_resistance = sum(sum_resistances)
            self.line_edit_fittings_total.setText(str(total_resistance))

            fittings = pd.DataFrame()
            fittings['name'] = names
            fittings['quantity'] = quantities
            fittings['K/f'] = resistances
            fittings['nL/D'] = sum_resistances
            self.fittings = fittings
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Fittings Table is Empty or Invalid!")

        #Verify Inputs
        try:
            line_description = self.line_description.text()
            nominal_size = self.nominal_size.text()
            material_and_schedule = self.material_and_schedule.text()
            epsilon = float(self.absolute_roughness.text())
            d = float(self.d.text())
            D = d / 1000
            self.D.setText(str(sf.round(D, 3)))
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Characteristics are Empty or Invalid!")

        #Get Fluid Properties
        if self.tab_fluid_properties.currentIndex() == 0:
            #Node Mode
            try:
                p1 = float(self.line_edit_source_p.text())
                t1 = float(self.line_edit_source_t.text())
                q1 = float(self.line_edit_source_q.text())
                h1 = float(self.line_edit_source_h.text())
                node1 = ps.node("Source Node", p1, t1, q1, h1)

                p2 = float(self.line_edit_source_p.text())
                t2 = float(self.line_edit_source_t.text())
                q2 = float(self.line_edit_source_q.text())
                h2 = float(self.line_edit_source_h.text())
                node2 = ps.node("Destination Node", p2, t2, q2, h2)

                if q1 != q2:
                    QMessageBox.warning(self, "Warning", "Mass Flow Rates are Different!")
                else:
                    q = q1

                p_avg = (node1.p + node2.p) / 2
                t_avg = (node1.t + node2.t) / 2
            except Exception as e:
                QMessageBox.warning(self, "Warning", "Node Properties are Empty or Invalid!")

        elif self.tab_fluid_properties.currentIndex() == 1:
            #Average Mode
            try:
                p_avg = float(self.line_edit_p_avg.text())
                t_avg = float(self.line_edit_t_avg.text())
                q = float(self.line_edit_q.text())
            except Exception as e:
                QMessageBox.warning(self, "Warning", "Average Properties are Empty or Invalid!")
        else:
            QMessageBox.warning(self, "Warning", "Fluid Properties Tab is Empty or Invalid!")

        try:
            L_p = float(self.line_edit_l_p.text())
            static_head_m = float(self.line_edit_static_head_m.text())
            misc_pressure_drop_m = float(self.line_edit_misc_m.text())

            pressure_drop, [D, p_avg, t_avg, V, my, vel, Re, f, turbulence, fitting_resistance, L_f, L_tel, h_l, dP, static_head, misc_pressure_drop] = ps.pressure_drop(p_avg, t_avg, q, d, epsilon, total_resistance, L_p, static_head_m, misc_pressure_drop_m)

            self.line_edit_V.setText(str(sf.round(V, 3)))
            self.line_edit_mu.setText(str(sf.round(my * 1000, 3)))
            self.line_edit_vel.setText(str(sf.round(vel, 3)))
            self.line_edit_vel2.setText(str(sf.round(vel * 60, 3)))
            self.line_edit_Re.setText(str(sf.round(Re,3)))
            self.line_edit_f.setText(str(sf.round(f,3)))
            self.line_edit_fluid_type.setText(str(turbulence))
            self.line_edit_l_f.setText(str(sf.round(L_f, 3)))
            self.line_edit_l_tel.setText(str(sf.round(L_tel, 3)))
            self.line_edit_h_l.setText(str(sf.round(h_l, 3)))
            self.line_edit_delta_p.setText(str(sf.round(dP, 3)))
            self.line_edit_static_head_bar.setText(str(sf.round(static_head, 3)))
            self.line_edit_misc_bar.setText(str(sf.round(misc_pressure_drop, 3)))
            self.line_edit_misc_bar.setText(str(sf.round(misc_pressure_drop, 3)))
            self.line_edit_pressure_drop.setText(str(sf.round(pressure_drop, 3)))

            self.data_dict = {
                "epsilon": epsilon,
                "d": d,
                "D": d / 1000,
                "flow_rate": q,
                "p_avg": p_avg,
                "t_avg": t_avg,
                "V": V,
                "mu": my,
                "Vel_m_sec": vel,
                "Vel_m_min": vel * 60,
                "Re": Re,
                "f": f,
                "turbulence": turbulence,
                "nL/D": resistance,
                "L_F": L_f,
                "L_P": L_p,
                "L_TEL": L_tel,
                "h_L": h_l,
                "dP": dP,
                "static_head_m": static_head_m,
                "static_head_bar": static_head,
                "misc_pressure_drop_m": misc_pressure_drop_m,
                "misc_pressure_drop_bar": misc_pressure_drop,
                "total_pressure_drop": pressure_drop,
                "line_description": line_description,
                "nominal_size": nominal_size,
                "material_and_schedule": material_and_schedule
            }
        except Exception as e:
            pass
    def pipe_to_excel(self):
        ps.pipe_to_excel(self.data_dict, self.fittings)

    def wall_autofill(self):
        p_avg = self.data_dict["p_avg"]
        p_avg = int(p_avg * 1.05)
        P = math.ceil(p_avg / 5) * 5

        t_avg = int(self.data_dict["t_avg"] + 5)
        T = math.ceil(t_avg / 5) * 5

        d = self.data_dict["d"]

        self.line_edit_pipeline_identification.setText(self.data_dict["line_description"])
        self.line_edit_design_pressure.setText(str(P))
        self.line_edit_design_temperature.setText(str(T))
        self.line_edit_internal_diameter.setText(str(d))

    def wall_calculate(self):
        P = float(self.line_edit_design_pressure.text())
        T = float(self.line_edit_design_temperature.text())
        d = float(self.line_edit_internal_diameter.text())
        SE = float(self.line_edit_SE.text())
        Y = float(self.line_edit_Y.text())
        A = float(self.line_edit_A.text())
        MFG = float(self.line_edit_MFG.text())
        BEND = float(self.line_edit_BEND.text())

        T_m = (P * d) / (2 * (SE + P*Y - P)) + A
        T_n = T_m /(1 - MFG) * BEND
        OD = d + 2 * T_m

        self.line_edit_P_display.setText(str(P))
        self.line_edit_t_m.setText(str(sf.round(T_m, 3)))
        self.line_edit_t_n.setText(str(sf.round(T_n, 3)))
        self.line_edit_OD.setText(str(sf.round(OD, 3)))

        pipeline_identification = self.line_edit_pipeline_identification.text()
        applicable_pipe_sizes = self.line_edit_applicable_pipes.text()
        BREI = self.line_edit_BREI.text()
        ASTM = self.line_edit_ASTM.text()
        fluid = self.line_edit_fluid.text()

        self.wall_dict = {
            "P": P,
            "T": T,
            "d": d,
            "SE": SE,
            "Y": Y,
            "A": A,
            "MFG": MFG,
            "BEND": BEND,
            "T_m": T_m,
            "T_n": T_n,
            "OD": OD,
            "pipeline_identification": pipeline_identification,
            "applicable_pipe_sizes": applicable_pipe_sizes,
            "BREI": BREI,
            "ASTM": ASTM,
            "fluid": fluid
        }
    
    def wall_to_excel(self):
        ps.wall_to_excel(self.wall_dict)
        
    def update_SE(self):
        ksi = float(self.line_edit_SE_ksi.text())
        bar = ps.to_bar(ksi)
        self.line_edit_SE.setText(str(sf.round(bar,5)))

    def update_fahrenheit(self):
        celsius = float(self.line_edit_design_temperature.text())
        fahrenheit = ps.to_fahrenheit(celsius)
        self.line_edit_fahrenheit.setText(str(sf.round(fahrenheit,5)))

    def update_capacity(self):
        try:
            st = XSteam(XSteam.UNIT_SYSTEM_MKS)
            temperature = float(self.line_edit_4.text())
            pressure = st.psat_t(temperature)
            specific_volume = st.vL_t(temperature)

            mass_flow_rate = float(self.line_edit_mass_flow_rate.text())
            capacity = mass_flow_rate * specific_volume

            self.line_edit_1.setText(str(capacity))
            self.line_edit_5.setText(str(sf.round(pressure,5)))
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Fluid Properties are Empty or Invalid!")

    def calculate_suction(self):
        st = XSteam(XSteam.UNIT_SYSTEM_MKS)
        temperature = float(self.line_edit_4.text())
        terminal_pressure = float(self.line_edit_6.text())
        specific_volume = st.vL_t(temperature)
        specific_gravity = (1 / specific_volume) / 1000
        meter_of_fluid_head = specific_volume * 100000 / 9.81
        static_head_m = float(self.line_edit_suction_static_head_m.text())
        static_head = static_head_m / meter_of_fluid_head
        equipment_loss = float(self.line_edit_10.text())
        piping_friction_loss = float(self.line_edit_11.text())
        margin_for_piping_loss = float(self.line_edit_12.text())
        total_piping_loss_with_margin = piping_friction_loss * (1 + margin_for_piping_loss/100)
        total_suction_pressure = terminal_pressure + static_head - equipment_loss - total_piping_loss_with_margin

        NPSHA_bar = total_suction_pressure - terminal_pressure
        NPSHA_m = NPSHA_bar * meter_of_fluid_head

        self.line_edit_7.setText(str(sf.round(specific_gravity, 5)))
        self.line_edit_8.setText(str(sf.round(meter_of_fluid_head, 5)))
        self.line_edit_9.setText(str(sf.round(static_head, 5)))
        self.line_edit_13.setText(str(sf.round(total_piping_loss_with_margin, 5)))
        self.line_edit_14.setText(str(sf.round(total_suction_pressure, 5)))
        self.line_edit_15.setText(str(sf.round(NPSHA_bar, 5)))
        self.line_edit_16.setText(str(sf.round(NPSHA_m, 5)))

    def calculate_discharge(self):
        st = XSteam(XSteam.UNIT_SYSTEM_MKS)
        temperature = float(self.line_edit_4.text())
        terminal_pressure = float(self.line_edit_17.text())
        specific_volume = st.vL_t(temperature)
        specific_gravity = (1 / specific_volume) / 1000
        meter_of_fluid_head = specific_volume * 100000 / 9.81
        static_head_m = float(self.line_edit_discharge_static_head_m.text())
        static_head = static_head_m / meter_of_fluid_head
        equipment_loss = float(self.line_edit_21.text())
        piping_friction_loss = float(self.line_edit_22.text())
        margin_for_piping_loss = float(self.line_edit_23.text())
        total_piping_loss_with_margin = piping_friction_loss * (1 + margin_for_piping_loss/100)
        control_valve_loss = float(self.line_edit_25.text())
        pump_wear = float(self.line_edit_26.text())
        total_discharge_pressure = terminal_pressure + static_head + equipment_loss + total_piping_loss_with_margin + control_valve_loss + pump_wear

        self.line_edit_18.setText(str(sf.round(specific_gravity,5)))
        self.line_edit_19.setText(str(sf.round(meter_of_fluid_head,5)))
        self.line_edit_20.setText(str(sf.round(static_head,5)))
        self.line_edit_24.setText(str(sf.round(total_piping_loss_with_margin,5)))
        self.line_edit_27.setText(str(sf.round(total_discharge_pressure,5)))


    def calculate_hydraulics(self):
        try:
            self.calculate_suction()
            self.calculate_discharge()
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Hydraulics Inputs are Empty or Invalid!")






                
            


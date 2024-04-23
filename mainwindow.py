from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from ui_mainwindow import Ui_MainWindow

import pipe_sizing as ps
from pyXSteam.XSteam import XSteam
import sigfig as sf
import pandas as pd
st = XSteam(XSteam.UNIT_SYSTEM_MKS)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.button_add_row.clicked.connect(self.add_row)
        self.button_remove_row.clicked.connect(self.delete_row)
        self.button_reset_rows.clicked.connect(self.reset_rows)

        self.button_pipe_calculate.clicked.connect(self.pipe_calculate)

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
            self.line_edit_fittings_total.setText(str(sum_resistances))

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
                node1 = ps.Node("Source Node", p1, t1, q1, h1)

                p2 = float(self.line_edit_source_p.text())
                t2 = float(self.line_edit_source_t.text())
                q2 = float(self.line_edit_source_q.text())
                h2 = float(self.line_edit_source_h.text())
                node2 = ps.Node("Destination Node", p2, t2, q2, h2)

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
                "total_pressure_drop": pressure_drop
            }
        except Exception as e:
            pass
    # def pipe_to_excel(self):
    #     ps.pipe_to_excel(self.data_dict, self.fittings)
    





                
            


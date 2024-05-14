import pandas as pd
import matplotlib.pyplot as plt
import os
import json

class Plotter:
    def __init__(self, json_path):
        self.json_path = json_path
        self.df = self.load_data()

    def load_data(self):
        with open(self.json_path, 'r') as file:
            data = json.load(file)
        df = pd.DataFrame(data)
        return df

    def draw_plots(self):
        plots_dir = "plots"
        os.makedirs(plots_dir, exist_ok=True)
        plot_paths = []

        # Выводим типы данных столбцов DataFrame для диагностики
        print("DataFrame dtypes:\n", self.df.dtypes)

        # Список столбцов для построения графиков
        columns_to_plot = [
            'mean', 'max', 'min', 'floor_mean', 'floor_max', 'floor_min',
            'ceiling_mean', 'ceiling_max', 'ceiling_min'
        ]
        
        for column in columns_to_plot:
            if column in self.df.columns:
                if pd.api.types.is_numeric_dtype(self.df[column]) and self.df[column].notna().sum() > 0:
                    plt.figure()
                    self.df[column].plot(kind='hist', bins=30, title=column)
                    plot_path = os.path.join(plots_dir, f"{column}.png")
                    plt.savefig(plot_path)
                    plot_paths.append(plot_path)
                    plt.close()
                else:
                    print(f"Column '{column}' is not numeric or has no data and will be skipped.")
            else:
                print(f"Column '{column}' not found in the DataFrame and will be skipped.")

        return plot_paths

# Проверка
# if __name__ == "__main__":
#     plotter = Plotter(json_path="../deviation.json")
#     plot_paths = plotter.draw_plots()
#     for path in plot_paths:
#         print(f"Plot saved to: {path}")


from diagrams import Diagram, Cluster
from diagrams.custom import Custom  # Customクラスを正しくインポート
import os

def create_diagram(base_path, image_names):
    image_paths = {key: os.path.join(base_path, val) for key, val in image_names.items()}
    missing_keys = [key for key, val in image_paths.items() if not os.path.exists(val)]
    
    if missing_keys:
        print(f"Warning: Missing images for keys {missing_keys}")

    with Diagram("図の説明", show=False):
        with Cluster("Cluster 1"):
            elderly = Custom("社長の思いつき", image_paths.get("elderly"))
            non_tech_boss = Custom("命令だけの部長", image_paths.get("non_tech_boss"))
            tech_boss = Custom("開発力のないIT部門", image_paths.get("tech_boss"))
            non_tech_boss >> tech_boss

        with Cluster("Cluster 2"):
            non_ai_engineer = Custom("AIはわからない大手SIer", image_paths.get("non_ai_engineer"))
            coder_1 = Custom("実績がない協力会社1", image_paths.get("coder_1"))
            coder_2 = Custom("仕事が遅い協力会社2", image_paths.get("coder_2"))
            non_ai_engineer >> coder_1 >> coder_2

        factory_worker = Custom("現場の無い現場監督", image_paths.get("factory_worker"))
        presenter = Custom("コンサルの無駄な提案", image_paths.get("presenter"))
        ai_product = Custom("独自のAIベンチャー", image_paths.get("ai_product"))
        catastrophe = Custom("フルーツランドジョージ", image_paths.get("catastrophe"))

        elderly >> non_tech_boss
        tech_boss >> non_ai_engineer
        coder_2 >> ai_product >> catastrophe

# 画像ファイル名とノード名の対応
image_names = {
    "elderly": "ojisan4.png",
    "non_tech_boss": "walking_businessman2.png",
    "tech_boss": "sensu_salaryman.png",
    "non_ai_engineer": "building_koujou_entotsu.png",
    "coder_1": "job_programmer.png",
    "coder_2": "job_sagyouin_computer_man.png",
    "factory_worker": "ai_shigoto.png",
    "presenter": "presentation_man.png",
    "ai_product": "nomad_surfing_nangoku.png",
    "catastrophe": "nomad_surfing_nangoku.png"
}

# 基本パス
base_path = "C:\\Users\\lemil\\developer\\diagrams\\resource"

# ダイアグラムの作成
create_diagram(base_path, image_names)

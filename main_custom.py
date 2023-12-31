from diagrams import Diagram, Cluster
from diagrams.custom import Custom
import os

def create_diagram(base_path, image_names):
    image_paths = {key: os.path.join(base_path, val) for key, val in image_names.items()}
    missing_keys = [key for key, val in image_paths.items() if not os.path.exists(val)]
    
    if missing_keys:
        print(f"Warning: Missing images for keys {missing_keys}")

    with Diagram("図の説明2", show=False):
        with Cluster("Cluster 1"):
            elderly = Custom("社長の思いつき", image_paths.get("elderly"))
            non_tech_boss = Custom("命令だけの部長", image_paths.get("non_tech_boss"))
            presenter = Custom("プロの驚き屋", image_paths.get("presenter"))
            elderly >> non_tech_boss << presenter

        with Cluster("Cluster 2"):
            tech_boss = Custom("外注するだけのIT部門", image_paths.get("tech_boss"))
            factory_worker = Custom("理解の無い現場", image_paths.get("factory_worker"))
            tech_boss << factory_worker
        
        with Cluster("Cluster 3"):
            non_ai_engineer = Custom("ノウハウがない大手SIer", image_paths.get("non_ai_engineer"), width="0.5", height="0.5")
            coder_1 = Custom("実績がほしい下請け1", image_paths.get("coder_1"), width="0.5", height="0.5")
            coder_2 = Custom("仕事がほしい下請け2", image_paths.get("coder_1"), width="0.5", height="0.5")            
            ai_product = Custom("謎のChatGPTスタートアップ", image_paths.get("ai_product"), width="0.5", height="0.5")
            catastrophe = Custom("フリーランスエンジニア", image_paths.get("catastrophe"), width="0.5", height="0.5")
            non_ai_engineer >> coder_1 >> coder_2 >> ai_product >> catastrophe

        non_tech_boss >> tech_boss
        tech_boss >> non_ai_engineer
        

# 画像ファイル名とノード名の対応
image_names = {
    "elderly": "sensu_salaryman.png",
    "non_tech_boss": "ojisan4.png",
    "tech_boss": "sensu_salaryman.png",
    "non_ai_engineer": "building_koujou_entotsu.png",
    "coder_1": "job_programmer.png",
    "coder_2": "job_sagyouin_computer_man.png",
    "factory_worker": "ai_shigoto.png",
    "presenter": "presentation_man.png",
    "ai_product": "ai_shigoto.png",
    "catastrophe": "nomad_surfing_nangoku.png"
}

# 基本パス
base_path = "C:\\Users\\papa\\development\\diagrams\\resource"

# ダイアグラムの作成
create_diagram(base_path, image_names)

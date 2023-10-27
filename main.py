from diagrams import Diagram, Cluster
from diagrams.custom import Custom
import os

def create_image_paths(base_path, image_names):
    return {key: os.path.join(base_path, val) for key, val in image_names.items()}

def check_missing_images(image_paths):
    missing_keys = [key for key, val in image_paths.items() if not os.path.exists(val)]
    if missing_keys:
        print(f"Warning: Missing images for keys {missing_keys}")

def create_diagram(base_path, image_names):
    image_paths = create_image_paths(base_path, image_names)
    check_missing_images(image_paths)

    common_graph_attrs = {"label": "", "color": "none", "penwidth": "0", "bgcolor": "none"}
    diagram_attrs = {
        "node_attr": {"fontname": "Meiryo UI", "fontsize": "12", "fontweight": "bold", "width": "1.2", "height": "1.2"},
        "graph_attr": {"labelloc": "t", "fontweight": "bold", "fontsize": "28", "fontname": "Meiryo UI"}
    }

    with Diagram("絶対に失敗するChatGPT導入プロジェクト in JTC", show=False, **diagram_attrs):
        with Cluster("Cluster 1", graph_attr=common_graph_attrs):
            elderly = Custom("社長の思いつき", image_paths.get("elderly"))
            non_tech_boss = Custom("命令だけの部長", image_paths.get("non_tech_boss"))
            presenter = Custom("プロの驚き屋", image_paths.get("presenter"))
            elderly >> non_tech_boss << presenter

        with Cluster("Cluster 2", graph_attr=common_graph_attrs):
            tech_boss = Custom("外注するだけのIT部門", image_paths.get("tech_boss"))
            factory_worker = Custom("理解の無い現場", image_paths.get("factory_worker"))
            tech_boss << factory_worker
        
        with Cluster("Cluster 3", graph_attr=common_graph_attrs):
            non_ai_engineer = Custom("ノウハウがない大手SIer", image_paths.get("non_ai_engineer"))
            coder_1 = Custom("実績がほしい下請け1", image_paths.get("coder_1"))
            coder_2 = Custom("仕事がほしい下請け2", image_paths.get("coder_1"))
            ai_product = Custom("謎のChatGPTスタートアップ", image_paths.get("ai_product"))
            catastrophe = Custom("フリーランスエンジニア", image_paths.get("catastrophe"))
            non_ai_engineer >> coder_1 >> coder_2 >> ai_product >> catastrophe

        non_tech_boss >> tech_boss
        tech_boss >> non_ai_engineer

image_names = {
    "elderly": "sensu_salaryman.png",
    "non_tech_boss": "ojisan4.png",
    "tech_boss": "job_sagyouin_computer_man.png",
    "non_ai_engineer": "walking_businessman2.png",
    "coder_1": "job_programmer.png",
    "coder_2": "job_sagyouin_computer_man.png",
    "factory_worker": "building_koujou_entotsu.png",
    "presenter": "presentation_man.png",
    "ai_product": "ai_shigoto.png",
    "catastrophe": "nomad_surfing_nangoku.png"
}

base_path = "C:\\Users\\papa\\development\\diagrams\\resource"
create_diagram(base_path, image_names)

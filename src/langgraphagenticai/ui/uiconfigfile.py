from configparser import ConfigParser #configparser is a class which help you to parse the text file

class Config:
    def __init__(self,config_file="src/langgraphagenticai/ui/uiconfig.ini"):
        self.config=ConfigParser() #reading the config file
        self.config.read(config_file)

    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(",") #THIS will have access of all the field in uiconfigfile.ini Through root node" default" 
        #split will remove the delimiter if multiple llm are there

    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(",")
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(",")
    
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE")
    
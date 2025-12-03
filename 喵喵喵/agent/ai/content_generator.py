import os
import json
import time

class ContentGenerator:
    def __init__(self):
        self.cache_dir = "cache"
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
    
    def make_cache_name(self, knowledge_point, difficulty):
        safe_name = knowledge_point.replace(" ", "_")
        return f"{safe_name}_{difficulty}.json"
    
    def read_cache(self, cache_name):
        cache_file = os.path.join(self.cache_dir, cache_name)
        
        if not os.path.exists(cache_file):
            return None
            
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                cache_data = json.load(f)
            return cache_data
        except:
            return None
    
    def save_cache(self, cache_name, data):
        cache_file = os.path.join(self.cache_dir, cache_name)
        
        try:
            with open(cache_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except:
            print("保存缓存失败")
    
    def generate_content(self, knowledge_point, difficulty="medium"):
        if not knowledge_point:
            return {"error": "知识点不能为空"}
        
        if difficulty not in ["easy", "medium", "hard"]:
            difficulty = "medium"  # 默认中等难度
        
        cache_name = self.make_cache_name(knowledge_point, difficulty)
        cache_result = self.read_cache(cache_name)
        
        if cache_result:
            print("从缓存中获取内容")
            return cache_result
        
        print("生成新的学习内容")
        result = self.create_content(knowledge_point, difficulty)
        
        self.save_cache(cache_name, result)
        
        return result
    
    def create_content(self, knowledge_point, difficulty):
        if difficulty == "easy":
            exercises = [
                {
                    "question": f"什么是{knowledge_point}？",
                    "type": "简答题",
                    "score": 10
                },
                {
                    "question": f"{knowledge_point}有什么特点？",
                    "type": "简答题", 
                    "score": 10
                }
            ]
            
            explanations = [
                f"{knowledge_point}是一个重要的概念。",
                f"学习{knowledge_point}需要掌握基本概念。"
            ]
            
        elif difficulty == "medium":
            exercises = [
                {
                    "question": f"{knowledge_point}有什么应用？",
                    "type": "分析题",
                    "score": 15
                },
                {
                    "question": f"比较{knowledge_point}和其他概念的异同",
                    "type": "比较题",
                    "score": 15
                }
            ]
            
            explanations = [
                f"{knowledge_point}有很多实际应用。",
                f"深入理解{knowledge_point}需要多练习。"
            ]
            
        else:
            exercises = [
                {
                    "question": f"设计一个使用{knowledge_point}的系统",
                    "type": "设计题", 
                    "score": 20
                },
                {
                    "question": f"分析{knowledge_point}的优缺点",
                    "type": "分析题",
                    "score": 20
                }
            ]
            
            explanations = [
                f"{knowledge_point}的高级应用比较复杂。",
                f"要精通{knowledge_point}需要深入学习。"
            ]
        
        return {
            "exercises": exercises,
            "explanations": explanations
        }
    
    def clear_cache(self):
        if os.path.exists(self.cache_dir):
            for file in os.listdir(self.cache_dir):
                if file.endswith('.json'):
                    os.remove(os.path.join(self.cache_dir, file))
            print("缓存已清理")
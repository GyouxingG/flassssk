import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from agent.ai.content_generator import ContentGenerator

def main():
    print("学习内容生成器")
    print("==============")
    
    generator = ContentGenerator()
    
    test_items = [
        {"knowledge_point": "Python编程", "difficulty": "easy"},
        {"knowledge_point": "人工智能", "difficulty": "medium"},
        {"knowledge_point": "机器学习", "difficulty": "hard"}
    ]
    
    for i, item in enumerate(test_items, 1):
        print(f"\n{i}. 知识点: {item['knowledge_point']}, 难度: {item['difficulty']}")
        print("-" * 40)
        
        result = generator.generate_content(item["knowledge_point"], item["difficulty"])
        
        if "error" in result:
            print(f"错误: {result['error']}")
        else:
            print("练习题:")
            for j, exercise in enumerate(result["exercises"], 1):
                print(f"  {j}. {exercise['question']} ({exercise['type']}, {exercise['score']}分)")
            
            print("\n解析:")
            for k, explanation in enumerate(result["explanations"], 1):
                print(f"  {k}. {explanation}")
    
    print("\n演示完成!")

if __name__ == "__main__":
    main()
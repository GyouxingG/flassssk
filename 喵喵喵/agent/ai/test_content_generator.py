import os
import sys
import shutil

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content_generator import ContentGenerator

def test_generate_content():
    print("测试生成内容功能...")
    
    test_cache = "test_cache"
    if not os.path.exists(test_cache):
        os.makedirs(test_cache)
    
    generator = ContentGenerator()
    generator.cache_dir = test_cache  # 使用测试缓存目录
    
    print("测试1: 正常生成内容")
    result = generator.generate_content("Python", "easy")
    
    if "exercises" in result and "explanations" in result:
        print("✓ 测试1通过")
    else:
        print("✗ 测试1失败")
        return False
    
    print("测试2: 缓存功能")
    result2 = generator.generate_content("Python", "easy")
    
    if result == result2:
        print("✓ 测试2通过")
    else:
        print("✗ 测试2失败")
        return False
    
    print("测试3: 不同难度")
    for difficulty in ["easy", "medium", "hard"]:
        result = generator.generate_content("测试", difficulty)
        if "exercises" in result:
            print(f"✓ {difficulty}难度测试通过")
        else:
            print(f"✗ {difficulty}难度测试失败")
            return False
    
    print("测试4: 参数检查")
    result = generator.generate_content("", "easy")
    if "error" in result:
        print("✓ 空知识点测试通过")
    else:
        print("✗ 空知识点测试失败")
        return False
    
    if os.path.exists(test_cache):
        shutil.rmtree(test_cache)
    
    print("所有测试通过!")
    return True

if __name__ == "__main__":
    test_generate_content()
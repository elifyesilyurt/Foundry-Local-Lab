import openai
from foundry_local import FoundryLocalManager

def main():
    print("Foundry Local Manager (Zeki Standart Model) başlatılıyor...")
    
    # 1. Bilgisayarında inik olan phi-3.5-mini modelini seçiyoruz
    alias = "phi-3.5-mini"
    manager = FoundryLocalManager(alias)
    
    print(f"Model bağlandı! API Uç Noktası: {manager.endpoint}")
    print("🤖 Model RAM'e yükleniyor ve yanıt üretiyor (Bu model biraz daha büyük olduğu için ilk açılış 5-10 sn sürebilir)...")
    
    try:
        # 2. Donanımımıza göre gerçek Model ID'sini çözüyoruz
        model_info = manager.get_model_info(alias)
        model_id = model_info.id if model_info else alias
        
        # 3. Standart OpenAI istemcisini yerel sunucumuza bağlıyoruz
        client = openai.OpenAI(base_url=manager.endpoint, api_key=manager.api_key)
        
        # 4. İsteğimizi gönderiyoruz
        response = client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": "Merhaba! Bilgisayarımda yerel olarak çalışan harika bir modelsin. Kendini kısaca tanıtır mısın?"}],
        )
        
        print("\n🤖 Phi-3.5-Mini'nin Yanıtı:")
        print(response.choices[0].message.content)
            
    except Exception as e:
        print(f"\nHata oluştu: {e}")

if __name__ == "__main__":
    main()

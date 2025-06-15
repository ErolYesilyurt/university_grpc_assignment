# 📚 University gRPC Sistemi

Bu proje, üniversite kütüphane sistemine ait kitap, öğrenci ve ödünç alma işlemlerinin yönetimi için bir gRPC sunucu-istemci uygulamasıdır.

## 🔧 Kullanılan Teknolojiler
- Python
- gRPC & Protocol Buffers

## 🏗️ Proje Yapısı
- `university.proto`: gRPC API tanımı.
- `src/server/`: Sunucu kodları.
- `src/client/`: İstemci kodları.
- `grpcurl-tests.md`: grpcurl test sonuçları.
- `DELIVERY.md`: Teslim raporu.

## ⚙️ Kurulum
```bash
python -m grpc_tools.protoc -I=. --python_out=src --grpc_python_out=src university.proto
python src/server.py
python src/client.py
```

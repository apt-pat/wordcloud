from PIL import Image

imagem = Image.open("3dprinter.png")

imagem_cinza = imagem.convert("L")

limiar = 200
imagem_binaria = imagem_cinza.point(lambda p: 0 if p < limiar else 255) 

imagem_binaria.save("mascara_invertida.png")

print("Máscara invertida salva como 'mascara_invertida.png'")
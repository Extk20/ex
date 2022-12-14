from tkinter import Image
from turtle import color
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
#from kivy.lang import Builder
#ko = Builder.load_file('ko.kv')
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
import pickle
#________________________________
import undetected_chromedriver.v2 as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

sound = SoundLoader.load('str\Music.wav')
if sound:
    sound.play()
Window.clearcolor = (0, 0.1, 0.1, 1.0)
Window.size = (400,600) 
Window.add_widget(Image(source="str/logo.png"))

greeting = Label(
    text="""Tiktok bot 2022 exclusive report 
from the programmer (0xfff0800)""",
    size_hint = (0.1,0.1),
    font_name = "Comic",
    pos_hint= {'x':0.45 , 'y':0.80},
    color = (1,1,1,2),
    )
Window.add_widget(greeting)
def cadastrar_credenciais(usuario=''):
    if usuario =='':
        usuario = input('what is the link ?')
    with open('conf.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write(f'{usuario}')

def ler_credenciais():
    with open('conf.txt', 'r', encoding='utf-8') as arquivo:
        usuario = arquivo.readlines()
    return usuario
def salvar_cookies(driver):
    driver = driver = uc.Chrome(use_subprocess=True)
    driver.get('https://www.tiktok.com/')
    time.sleep(60)
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    print('Cookies Salvos!')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    salvar_cookies(driver)
    for cookie in cookies:
        driver.add_cookie(cookie)


def any_Function(instance):
    usuario = ler_credenciais()
    driver = uc.Chrome()        
    try:
      for usuario in usuario:
       while True:
          driver.get(''+usuario+'')
          agree_btn_0 = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div[3]')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div[3]/div/div/div[1]/div')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//form/div[2]/label[1]/div')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//form/div[2]/label[4]')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//form/div[2]/label[2]/div')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//form/div[2]/div[3]/button')
          agree_btn_0.click()
          time.sleep(0.60)
    except:
        pass

def Function(instance):
    usuario = ler_credenciais()
    driver = uc.Chrome()
    try:
      for usuario in usuario:
       while True:
          driver.get(''+usuario+'')
          agree_btn_0 = driver.find_element(By.ID,'app')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[3]/div[1]/div[4]')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//form/div[2]/label[5]/div')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//form/div[2]/label[1]')
          agree_btn_0.click()
          time.sleep(0.60)
          agree_btn_0 = driver.find_element(By.XPATH,'//form/div[2]/div[3]/button')
          agree_btn_0.click()
          time.sleep(0.60)
    except:
        pass

class Myapp(App):
    def build(self):
        self.title = "Tiktok"
        button1 = Button(
            text = 'video',
            size_hint = (0.3,0.1),
            pos_hint= {'x':0.33 , 'y':0.2},
            color = (1,1,1,2),
            background_color= (0,0,0,6),
        )
        button1.bind(on_press=Function)
        button2 = Button(
            text = 'account',
            size_hint = (0.3,0.1),
            pos_hint= {'x':0.35 , 'y':0.2},
            color = (1,1,1,2),
            background_color= (0,0,0,6)
        )
        button3 = Button(
            text = 'Login TikTok',
            size_hint = (0.3,0.1),
            pos_hint= {'x':0.40 , 'y':0.2},
            color = (1,1,1,2),
            background_color= (0,0,0,6)
        )
        button2.bind(on_press=any_Function)
        button3.bind(on_press=salvar_cookies)
        boxlayout = BoxLayout()
        boxlayout.add_widget(button1)
        boxlayout.add_widget(button2)
        boxlayout.add_widget(button3)
        return boxlayout


if __name__ == '__main__':
    Myapp().run()



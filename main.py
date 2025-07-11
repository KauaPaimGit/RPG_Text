"""
RPG Épico - Versão Mobile Android
Arquivo principal para geração de APK
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.uix.progressbar import ProgressBar
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.core.audio import SoundLoader
from kivy.utils import get_color_from_hex
from kivy.metrics import dp, sp
import json
import os
import random

# Configurações para mobile
Window.size = (360, 640)  # Tamanho padrão mobile
Window.clearcolor = get_color_from_hex('#1a252f')

class MobileDataManager:
    """Gerenciador de dados para versão mobile"""
    
    @staticmethod
    def get_save_path():
        """Retorna caminho de save compatível com Android"""
        try:
            from android.storage import primary_external_storage_path
            return os.path.join(primary_external_storage_path(), 'RPGEpico')
        except:
            return os.path.join(os.path.expanduser('~'), 'RPGEpico')
    
    @staticmethod
    def salvar_jogo(jogador):
        """Salva o jogo na memória do dispositivo"""
        try:
            save_dir = MobileDataManager.get_save_path()
            os.makedirs(save_dir, exist_ok=True)
            
            save_file = os.path.join(save_dir, 'save_mobile.json')
            with open(save_file, 'w', encoding='utf-8') as f:
                json.dump(jogador, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Erro ao salvar: {e}")
            return False
    
    @staticmethod
    def carregar_jogo():
        """Carrega o jogo salvo"""
        try:
            save_file = os.path.join(MobileDataManager.get_save_path(), 'save_mobile.json')
            if os.path.exists(save_file):
                with open(save_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar: {e}")
        
        # Jogador padrão
        return {
            "nome": "Aventureiro",
            "nivel": 1,
            "xp": 0,
            "vida": 100,
            "vida_max": 100,
            "mana": 50,
            "mana_max": 50,
            "ataque": 10,
            "defesa": 5,
            "ouro": 500,
            "equipamentos": {},
            "mascotes": {},
            "montarias": {},
            "inventario": {},
            "conquistas": [],
            "configuracoes": {
                "volume": 0.7,
                "tema": "dark_epic"
            }
        }

class MobileMascoteSystem:
    """Sistema de mascotes adaptado para mobile"""
    
    @staticmethod
    def criar_mascotes_mobile():
        """Versão otimizada dos mascotes para mobile"""
        return {
            # Mascotes Comuns
            "gato_preto": {
                "nome": "Gato Sombrio",
                "emoji": "🐱",
                "raridade": "Comum",
                "poder": 100,
                "bonus": {"agilidade": 2, "stealth": 5},
                "habilidades": ["Caminhada Silenciosa", "Visão Noturna"],
                "custo": 50,
                "descricao": "Felino misterioso das sombras",
                "evolucoes": ["felino_sombrio"],
                "cor": "#95a5a6"
            },
            "corvo_mensageiro": {
                "nome": "Corvo Arcano",
                "emoji": "🐦‍⬛",
                "raridade": "Comum", 
                "poder": 120,
                "bonus": {"inteligencia": 3, "velocidade": 2},
                "habilidades": ["Entrega Rápida", "Visão Aérea"],
                "custo": 75,
                "descricao": "Corvo inteligente e veloz",
                "evolucoes": ["corvo_arcano"],
                "cor": "#95a5a6"
            },
            "coelho_lunar": {
                "nome": "Coelho da Lua",
                "emoji": "🐰",
                "raridade": "Comum",
                "poder": 90,
                "bonus": {"sorte": 5, "agilidade": 3},
                "habilidades": ["Salto Alto", "Bênção Lunar"],
                "custo": 60,
                "descricao": "Coelho mágico da boa sorte",
                "evolucoes": ["coelho_celeste"],
                "cor": "#95a5a6"
            },
            
            # Mascotes Incomuns
            "lobo_gelo": {
                "nome": "Lobo Glacial",
                "emoji": "🐺",
                "raridade": "Incomum",
                "poder": 250,
                "bonus": {"ataque": 5, "resistencia": 10},
                "habilidades": ["Uivo Congelante", "Mordida Gélida"],
                "custo": 150,
                "descricao": "Lobo adaptado ao frio extremo",
                "evolucoes": ["lobo_ancestral"],
                "cor": "#27ae60"
            },
            "aguia_dourada": {
                "nome": "Águia Real",
                "emoji": "🦅",
                "raridade": "Incomum",
                "poder": 300,
                "bonus": {"visao": 10, "velocidade": 7},
                "habilidades": ["Voo Supersônico", "Garra Real"],
                "custo": 180,
                "descricao": "Majestosa águia dourada",
                "evolucoes": ["aguia_imperial"],
                "cor": "#27ae60"
            },
            
            # Mascotes Raros
            "dragao_bebe": {
                "nome": "Dragão Jovem",
                "emoji": "🐲",
                "raridade": "Raro",
                "poder": 500,
                "bonus": {"ataque": 8, "defesa": 6, "mana": 15},
                "habilidades": ["Sopro de Fogo", "Escamas Mágicas"],
                "custo": 500,
                "descricao": "Dragão com potencial infinito",
                "evolucoes": ["dragao_ancestral"],
                "cor": "#3498db"
            },
            "unicornio_prata": {
                "nome": "Unicórnio Divino",
                "emoji": "🦄",
                "raridade": "Raro",
                "poder": 600,
                "bonus": {"cura": 12, "purificacao": 10, "mana": 20},
                "habilidades": ["Cura Divina", "Luz Purificadora"],
                "custo": 600,
                "descricao": "Criatura pura e sagrada",
                "evolucoes": ["unicornio_celestial"],
                "cor": "#3498db"
            },
            
            # Mascotes Épicos
            "dragao_ancestral": {
                "nome": "Dragão Ancestral",
                "emoji": "🐉",
                "raridade": "Épico",
                "poder": 1200,
                "bonus": {"ataque": 15, "defesa": 12, "mana": 25},
                "habilidades": ["Sopro Devastador", "Rugido Real", "Voo Majestoso"],
                "custo": 1500,
                "descricao": "Dragão de poder ancestral",
                "evolucoes": ["dragao_divino"],
                "cor": "#9b59b6"
            },
            "fenix_imortal": {
                "nome": "Fênix Eterna",
                "emoji": "🔥",
                "raridade": "Épico",
                "poder": 1500,
                "bonus": {"regeneracao": 30, "fogo": 20},
                "habilidades": ["Renascimento", "Chamas Eternas"],
                "custo": 1800,
                "descricao": "Ave imortal das chamas",
                "evolucoes": [],
                "cor": "#9b59b6"
            },
            
            # Mascotes Lendários
            "dragao_divino": {
                "nome": "Dragão Cósmico",
                "emoji": "🐲",
                "raridade": "Lendário",
                "poder": 3000,
                "bonus": {"poder_total": 50, "sabedoria": 30},
                "habilidades": ["Sopro Cósmico", "Magia Antiga", "Transcendência"],
                "custo": 5000,
                "descricao": "Dragão que transcendeu a mortalidade",
                "evolucoes": [],
                "cor": "#f39c12"
            },
            "kitsune_suprema": {
                "nome": "Kitsune Suprema",
                "emoji": "🦊",
                "raridade": "Lendário",
                "poder": 3500,
                "bonus": {"magia": 35, "tempo": 20, "sabedoria": 25},
                "habilidades": ["Manipulação Temporal", "Ilusão Perfeita"],
                "custo": 8000,
                "descricao": "Kitsune que domina o tempo",
                "evolucoes": [],
                "cor": "#f39c12"
            },
            
            # Mascotes Míticos
            "bahamut": {
                "nome": "Bahamut - Rei Dragão",
                "emoji": "🐲",
                "raridade": "Mítico",
                "poder": 10000,
                "bonus": {"poder_absoluto": 100, "realeza": 50},
                "habilidades": ["Sopro Galáctico", "Comando Supremo", "Criação"],
                "custo": 20000,
                "descricao": "O supremo rei de todos os dragões",
                "evolucoes": [],
                "cor": "#e74c3c"
            }
        }
    
    @staticmethod
    def comprar_mascote(mascote_id, jogador):
        """Compra um mascote"""
        mascotes_data = MobileMascoteSystem.criar_mascotes_mobile()
        
        if mascote_id not in mascotes_data:
            return False, "Mascote não encontrado!"
        
        data = mascotes_data[mascote_id]
        custo = data["custo"]
        
        if jogador.get("ouro", 0) < custo:
            return False, f"Você precisa de {custo} ouro!"
        
        if mascote_id in jogador.get("mascotes", {}):
            return False, "Você já possui este mascote!"
        
        # Realizar compra
        jogador["ouro"] -= custo
        if "mascotes" not in jogador:
            jogador["mascotes"] = {}
        
        jogador["mascotes"][mascote_id] = {
            "nivel": 1,
            "xp": 0,
            "ativo": True
        }
        
        MobileDataManager.salvar_jogo(jogador)
        return True, f"Você adquiriu {data['nome']}!"

class MobileMountSystem:
    """Sistema de montarias para mobile"""
    
    @staticmethod
    def criar_montarias_mobile():
        """Montarias otimizadas para mobile"""
        return {
            "cavalo_guerra": {
                "nome": "Cavalo de Guerra",
                "emoji": "🐎",
                "tipo": "Terrestre",
                "velocidade": 150,
                "resistencia": 100,
                "custo": 200,
                "descricao": "Cavalo robusto para batalhas",
                "cor": "#95a5a6"
            },
            "lobo_gigante": {
                "nome": "Lobo Gigante",
                "emoji": "🐺",
                "tipo": "Terrestre",
                "velocidade": 200,
                "resistencia": 120,
                "custo": 400,
                "descricao": "Lobo feroz e veloz",
                "cor": "#27ae60"
            },
            "aguia_gigante": {
                "nome": "Águia Gigante",
                "emoji": "🦅",
                "tipo": "Voador",
                "velocidade": 300,
                "resistencia": 80,
                "custo": 800,
                "descricao": "Voa pelos céus rapidamente",
                "cor": "#3498db"
            },
            "dragao_voador": {
                "nome": "Dragão Voador",
                "emoji": "🐉",
                "tipo": "Voador",
                "velocidade": 500,
                "resistencia": 200,
                "custo": 2000,
                "descricao": "Majestoso dragão dos céus",
                "cor": "#9b59b6"
            },
            "unicornio_alado": {
                "nome": "Unicórnio Alado",
                "emoji": "🦄",
                "tipo": "Mágico",
                "velocidade": 400,
                "resistencia": 150,
                "custo": 3000,
                "descricao": "Unicórnio com asas divinas",
                "cor": "#f39c12"
            },
            "fenix_montaria": {
                "nome": "Fênix Suprema",
                "emoji": "🔥",
                "tipo": "Lendário",
                "velocidade": 800,
                "resistencia": 300,
                "custo": 10000,
                "descricao": "A mais rápida de todas as montarias",
                "cor": "#e74c3c"
            }
        }

class MobileAudioManager:
    """Gerenciador de áudio otimizado para mobile"""
    
    def __init__(self):
        self.sounds = {}
        self.volume = 0.7
        self.enabled = True
    
    def load_sound(self, name, file_path):
        """Carrega um som"""
        try:
            if os.path.exists(file_path):
                sound = SoundLoader.load(file_path)
                if sound:
                    self.sounds[name] = sound
        except Exception as e:
            print(f"Erro ao carregar som {name}: {e}")
    
    def play_sound(self, name):
        """Toca um som"""
        if not self.enabled or name not in self.sounds:
            return
        
        try:
            sound = self.sounds[name]
            sound.volume = self.volume
            sound.play()
        except Exception as e:
            print(f"Erro ao tocar som {name}: {e}")
    
    def set_volume(self, volume):
        """Define o volume"""
        self.volume = max(0.0, min(1.0, volume))

# Instância global do audio manager
audio_manager = MobileAudioManager()

class MenuPrincipalScreen(Screen):
    """Tela do menu principal"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jogador = MobileDataManager.carregar_jogo()
        self.build_ui()
    
    def build_ui(self):
        """Constrói a interface"""
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Título épico
        title = Label(
            text='🐲 RPG ÉPICO MOBILE 🦄',
            font_size=sp(28),
            bold=True,
            color=get_color_from_hex('#f39c12'),
            size_hint_y=None,
            height=dp(80)
        )
        layout.add_widget(title)
        
        # Status do jogador
        status_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(100))
        
        # Informações básicas
        info_layout = BoxLayout(orientation='vertical')
        
        nome_label = Label(
            text=f"👤 {self.jogador['nome']} - Nível {self.jogador['nivel']}",
            font_size=sp(16),
            bold=True,
            color=get_color_from_hex('#3498db')
        )
        info_layout.add_widget(nome_label)
        
        ouro_label = Label(
            text=f"💰 {self.jogador['ouro']} Ouro",
            font_size=sp(14),
            color=get_color_from_hex('#f1c40f')
        )
        info_layout.add_widget(ouro_label)
        
        vida_label = Label(
            text=f"❤️ {self.jogador['vida']}/{self.jogador['vida_max']} HP",
            font_size=sp(14),
            color=get_color_from_hex('#e74c3c')
        )
        info_layout.add_widget(vida_label)
        
        status_layout.add_widget(info_layout)
        layout.add_widget(status_layout)
        
        # Botões principais
        buttons_data = [
            ("🎮 AVENTURA", self.ir_aventura, '#27ae60'),
            ("🐱 MASCOTES", self.ir_mascotes, '#9b59b6'),
            ("🐎 MONTARIAS", self.ir_montarias, '#34495e'),
            ("🎒 INVENTÁRIO", self.ir_inventario, '#2980b9'),
            ("⚔️ EQUIPAMENTOS", self.ir_equipamentos, '#c0392b'),
            ("🏆 CONQUISTAS", self.ir_conquistas, '#f39c12'),
            ("⚙️ CONFIGURAÇÕES", self.ir_configuracoes, '#95a5a6')
        ]
        
        for text, callback, color in buttons_data:
            btn = Button(
                text=text,
                font_size=sp(18),
                bold=True,
                background_color=get_color_from_hex(color),
                size_hint_y=None,
                height=dp(60)
            )
            btn.bind(on_press=callback)
            layout.add_widget(btn)
        
        self.add_widget(layout)
    
    def ir_aventura(self, instance):
        """Vai para aventura"""
        audio_manager.play_sound('click')
        self.manager.current = 'aventura'
    
    def ir_mascotes(self, instance):
        """Vai para mascotes"""
        audio_manager.play_sound('click')
        self.manager.current = 'mascotes'
    
    def ir_montarias(self, instance):
        """Vai para montarias"""
        audio_manager.play_sound('click')
        self.manager.current = 'montarias'
    
    def ir_inventario(self, instance):
        """Vai para inventário"""
        audio_manager.play_sound('click')
        self.manager.current = 'inventario'
    
    def ir_equipamentos(self, instance):
        """Vai para equipamentos"""
        audio_manager.play_sound('click')
        self.manager.current = 'equipamentos'
    
    def ir_conquistas(self, instance):
        """Vai para conquistas"""
        audio_manager.play_sound('click')
        self.manager.current = 'conquistas'
    
    def ir_configuracoes(self, instance):
        """Vai para configurações"""
        audio_manager.play_sound('click')
        self.manager.current = 'configuracoes'

class MascotesScreen(Screen):
    """Tela de mascotes"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jogador = MobileDataManager.carregar_jogo()
        self.build_ui()
    
    def build_ui(self):
        """Constrói interface de mascotes"""
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))
        
        voltar_btn = Button(
            text='🔙',
            font_size=sp(24),
            size_hint_x=None,
            width=dp(60),
            background_color=get_color_from_hex('#95a5a6')
        )
        voltar_btn.bind(on_press=self.voltar)
        header.add_widget(voltar_btn)
        
        title = Label(
            text='🐲 MASCOTES ÉPICOS 🦄',
            font_size=sp(20),
            bold=True,
            color=get_color_from_hex('#f39c12')
        )
        header.add_widget(title)
        
        layout.add_widget(header)
        
        # Scroll com mascotes
        scroll = ScrollView()
        mascotes_layout = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        mascotes_layout.bind(minimum_height=mascotes_layout.setter('height'))
        
        # Mostrar mascotes disponíveis
        mascotes_data = MobileMascoteSystem.criar_mascotes_mobile()
        mascotes_jogador = self.jogador.get("mascotes", {})
        
        for mascote_id, data in mascotes_data.items():
            possui = mascote_id in mascotes_jogador
            
            card = self.criar_card_mascote(mascote_id, data, possui)
            mascotes_layout.add_widget(card)
        
        scroll.add_widget(mascotes_layout)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def criar_card_mascote(self, mascote_id, data, possui):
        """Cria card de mascote"""
        card = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=dp(120),
            padding=dp(10),
            spacing=dp(5)
        )
        card.canvas.before.clear()
        
        with card.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(rgba=get_color_from_hex(data['cor']) + [0.2])
            card.rect = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[dp(10)]
            )
        
        card.bind(pos=self.update_rect, size=self.update_rect)
        
        # Header do card
        header_layout = BoxLayout(orientation='horizontal')
        
        nome_label = Label(
            text=f"{data['emoji']} {data['nome']}",
            font_size=sp(16),
            bold=True,
            color=get_color_from_hex('#ffffff')
        )
        header_layout.add_widget(nome_label)
        
        raridade_label = Label(
            text=data['raridade'],
            font_size=sp(12),
            color=get_color_from_hex(data['cor']),
            size_hint_x=None,
            width=dp(80)
        )
        header_layout.add_widget(raridade_label)
        
        card.add_widget(header_layout)
        
        # Informações
        info_label = Label(
            text=f"💪 Poder: {data['poder']} | 💰 {data['custo']} Ouro",
            font_size=sp(12),
            color=get_color_from_hex('#bdc3c7')
        )
        card.add_widget(info_label)
        
        desc_label = Label(
            text=data['descricao'],
            font_size=sp(10),
            color=get_color_from_hex('#95a5a6'),
            text_size=(dp(300), None),
            halign='center'
        )
        card.add_widget(desc_label)
        
        # Botão de ação
        if possui:
            status_btn = Button(
                text='✅ POSSUÍDO',
                font_size=sp(12),
                background_color=get_color_from_hex('#27ae60'),
                size_hint_y=None,
                height=dp(30)
            )
            status_btn.bind(on_press=lambda x: self.gerenciar_mascote(mascote_id))
        else:
            pode_comprar = self.jogador.get("ouro", 0) >= data["custo"]
            cor = '#3498db' if pode_comprar else '#95a5a6'
            
            status_btn = Button(
                text=f'💳 COMPRAR ({data["custo"]} 🪙)',
                font_size=sp(12),
                background_color=get_color_from_hex(cor),
                size_hint_y=None,
                height=dp(30),
                disabled=not pode_comprar
            )
            status_btn.bind(on_press=lambda x: self.comprar_mascote(mascote_id))
        
        card.add_widget(status_btn)
        
        return card
    
    def update_rect(self, instance, value):
        """Atualiza retângulo do card"""
        if hasattr(instance, 'rect'):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
    
    def comprar_mascote(self, mascote_id):
        """Compra um mascote"""
        sucesso, mensagem = MobileMascoteSystem.comprar_mascote(mascote_id, self.jogador)
        
        if sucesso:
            audio_manager.play_sound('success')
            self.mostrar_popup("Sucesso!", mensagem, self.atualizar_tela)
        else:
            audio_manager.play_sound('error')
            self.mostrar_popup("Erro!", mensagem)
    
    def gerenciar_mascote(self, mascote_id):
        """Gerencia mascote possuído"""
        mascotes_data = MobileMascoteSystem.criar_mascotes_mobile()
        data = mascotes_data[mascote_id]
        
        popup_content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        info_label = Label(
            text=f"{data['emoji']} {data['nome']}\n{data['descricao']}",
            font_size=sp(14),
            halign='center'
        )
        popup_content.add_widget(info_label)
        
        mascote_info = self.jogador["mascotes"][mascote_id]
        nivel = mascote_info.get("nivel", 1)
        ativo = mascote_info.get("ativo", False)
        
        status_label = Label(
            text=f"Nível: {nivel}\nStatus: {'🟢 Ativo' if ativo else '🔴 Inativo'}",
            font_size=sp(12)
        )
        popup_content.add_widget(status_label)
        
        # Botões
        btn_layout = BoxLayout(orientation='horizontal', spacing=dp(10))
        
        toggle_btn = Button(
            text='🔇 Desativar' if ativo else '🔊 Ativar',
            size_hint_y=None,
            height=dp(40)
        )
        toggle_btn.bind(on_press=lambda x: self.toggle_mascote(mascote_id))
        btn_layout.add_widget(toggle_btn)
        
        fechar_btn = Button(
            text='✖️ Fechar',
            size_hint_y=None,
            height=dp(40),
            background_color=get_color_from_hex('#95a5a6')
        )
        btn_layout.add_widget(fechar_btn)
        
        popup_content.add_widget(btn_layout)
        
        popup = Popup(
            title=f'Gerenciar {data["nome"]}',
            content=popup_content,
            size_hint=(0.9, 0.6)
        )
        
        fechar_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def toggle_mascote(self, mascote_id):
        """Ativa/desativa mascote"""
        mascotes = self.jogador.get("mascotes", {})
        if mascote_id in mascotes:
            ativo_atual = mascotes[mascote_id].get("ativo", False)
            mascotes[mascote_id]["ativo"] = not ativo_atual
            MobileDataManager.salvar_jogo(self.jogador)
            audio_manager.play_sound('success')
            self.atualizar_tela()
    
    def mostrar_popup(self, titulo, mensagem, callback=None):
        """Mostra popup de mensagem"""
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        label = Label(
            text=mensagem,
            font_size=sp(14),
            halign='center',
            valign='center'
        )
        content.add_widget(label)
        
        ok_btn = Button(
            text='OK',
            size_hint_y=None,
            height=dp(40),
            background_color=get_color_from_hex('#3498db')
        )
        content.add_widget(ok_btn)
        
        popup = Popup(
            title=titulo,
            content=content,
            size_hint=(0.8, 0.4)
        )
        
        def on_ok(instance):
            popup.dismiss()
            if callback:
                callback()
        
        ok_btn.bind(on_press=on_ok)
        popup.open()
    
    def atualizar_tela(self):
        """Atualiza a tela"""
        self.clear_widgets()
        self.jogador = MobileDataManager.carregar_jogo()
        self.build_ui()
    
    def voltar(self, instance):
        """Volta ao menu principal"""
        audio_manager.play_sound('click')
        self.manager.current = 'menu'

class MontariasScreen(Screen):
    """Tela de montarias"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jogador = MobileDataManager.carregar_jogo()
        self.build_ui()
    
    def build_ui(self):
        """Constrói interface de montarias"""
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))
        
        voltar_btn = Button(
            text='🔙',
            font_size=sp(24),
            size_hint_x=None,
            width=dp(60),
            background_color=get_color_from_hex('#95a5a6')
        )
        voltar_btn.bind(on_press=self.voltar)
        header.add_widget(voltar_btn)
        
        title = Label(
            text='🐎 MONTARIAS ÉPICAS 🐉',
            font_size=sp(20),
            bold=True,
            color=get_color_from_hex('#f39c12')
        )
        header.add_widget(title)
        
        layout.add_widget(header)
        
        # Scroll com montarias
        scroll = ScrollView()
        montarias_layout = GridLayout(cols=1, spacing=dp(10), size_hint_y=None)
        montarias_layout.bind(minimum_height=montarias_layout.setter('height'))
        
        # Mostrar montarias disponíveis
        montarias_data = MobileMountSystem.criar_montarias_mobile()
        montarias_jogador = self.jogador.get("montarias", {})
        
        for montaria_id, data in montarias_data.items():
            possui = montaria_id in montarias_jogador
            
            card = self.criar_card_montaria(montaria_id, data, possui)
            montarias_layout.add_widget(card)
        
        scroll.add_widget(montarias_layout)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def criar_card_montaria(self, montaria_id, data, possui):
        """Cria card de montaria"""
        card = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=dp(120),
            padding=dp(10),
            spacing=dp(5)
        )
        card.canvas.before.clear()
        
        with card.canvas.before:
            from kivy.graphics import Color, RoundedRectangle
            Color(rgba=get_color_from_hex(data['cor']) + [0.2])
            card.rect = RoundedRectangle(
                pos=card.pos,
                size=card.size,
                radius=[dp(10)]
            )
        
        card.bind(pos=self.update_rect, size=self.update_rect)
        
        # Header do card
        header_layout = BoxLayout(orientation='horizontal')
        
        nome_label = Label(
            text=f"{data['emoji']} {data['nome']}",
            font_size=sp(16),
            bold=True,
            color=get_color_from_hex('#ffffff')
        )
        header_layout.add_widget(nome_label)
        
        tipo_label = Label(
            text=data['tipo'],
            font_size=sp(12),
            color=get_color_from_hex(data['cor']),
            size_hint_x=None,
            width=dp(80)
        )
        header_layout.add_widget(tipo_label)
        
        card.add_widget(header_layout)
        
        # Informações
        info_label = Label(
            text=f"⚡ Velocidade: {data['velocidade']} | 🛡️ Resistência: {data['resistencia']}",
            font_size=sp(12),
            color=get_color_from_hex('#bdc3c7')
        )
        card.add_widget(info_label)
        
        desc_label = Label(
            text=f"💰 {data['custo']} Ouro - {data['descricao']}",
            font_size=sp(10),
            color=get_color_from_hex('#95a5a6'),
            text_size=(dp(300), None),
            halign='center'
        )
        card.add_widget(desc_label)
        
        # Botão de ação
        if possui:
            status_btn = Button(
                text='✅ POSSUÍDA',
                font_size=sp(12),
                background_color=get_color_from_hex('#27ae60'),
                size_hint_y=None,
                height=dp(30)
            )
            status_btn.bind(on_press=lambda x: self.usar_montaria(montaria_id))
        else:
            pode_comprar = self.jogador.get("ouro", 0) >= data["custo"]
            cor = '#3498db' if pode_comprar else '#95a5a6'
            
            status_btn = Button(
                text=f'💳 COMPRAR ({data["custo"]} 🪙)',
                font_size=sp(12),
                background_color=get_color_from_hex(cor),
                size_hint_y=None,
                height=dp(30),
                disabled=not pode_comprar
            )
            status_btn.bind(on_press=lambda x: self.comprar_montaria(montaria_id))
        
        card.add_widget(status_btn)
        
        return card
    
    def update_rect(self, instance, value):
        """Atualiza retângulo do card"""
        if hasattr(instance, 'rect'):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
    
    def comprar_montaria(self, montaria_id):
        """Compra uma montaria"""
        montarias_data = MobileMountSystem.criar_montarias_mobile()
        
        if montaria_id not in montarias_data:
            return
        
        data = montarias_data[montaria_id]
        custo = data["custo"]
        
        if self.jogador.get("ouro", 0) < custo:
            audio_manager.play_sound('error')
            self.mostrar_popup("Erro!", f"Você precisa de {custo} ouro!")
            return
        
        if montaria_id in self.jogador.get("montarias", {}):
            audio_manager.play_sound('error')
            self.mostrar_popup("Erro!", "Você já possui esta montaria!")
            return
        
        # Realizar compra
        self.jogador["ouro"] -= custo
        if "montarias" not in self.jogador:
            self.jogador["montarias"] = {}
        
        self.jogador["montarias"][montaria_id] = {
            "durabilidade": 100,
            "ativa": False
        }
        
        MobileDataManager.salvar_jogo(self.jogador)
        audio_manager.play_sound('success')
        self.mostrar_popup("Sucesso!", f"Você adquiriu {data['nome']}!", self.atualizar_tela)
    
    def usar_montaria(self, montaria_id):
        """Usa/gerencia uma montaria"""
        montarias_data = MobileMountSystem.criar_montarias_mobile()
        data = montarias_data[montaria_id]
        
        # Desativar outras montarias
        for mid in self.jogador.get("montarias", {}):
            self.jogador["montarias"][mid]["ativa"] = False
        
        # Ativar esta montaria
        self.jogador["montarias"][montaria_id]["ativa"] = True
        
        MobileDataManager.salvar_jogo(self.jogador)
        audio_manager.play_sound('success')
        self.mostrar_popup("Montaria Ativada!", f"Você está montando {data['nome']}!")
    
    def mostrar_popup(self, titulo, mensagem, callback=None):
        """Mostra popup de mensagem"""
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        label = Label(
            text=mensagem,
            font_size=sp(14),
            halign='center',
            valign='center'
        )
        content.add_widget(label)
        
        ok_btn = Button(
            text='OK',
            size_hint_y=None,
            height=dp(40),
            background_color=get_color_from_hex('#3498db')
        )
        content.add_widget(ok_btn)
        
        popup = Popup(
            title=titulo,
            content=content,
            size_hint=(0.8, 0.4)
        )
        
        def on_ok(instance):
            popup.dismiss()
            if callback:
                callback()
        
        ok_btn.bind(on_press=on_ok)
        popup.open()
    
    def atualizar_tela(self):
        """Atualiza a tela"""
        self.clear_widgets()
        self.jogador = MobileDataManager.carregar_jogo()
        self.build_ui()
    
    def voltar(self, instance):
        """Volta ao menu principal"""
        audio_manager.play_sound('click')
        self.manager.current = 'menu'

class ConfiguracoesScreen(Screen):
    """Tela de configurações"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jogador = MobileDataManager.carregar_jogo()
        self.build_ui()
    
    def build_ui(self):
        """Constrói interface de configurações"""
        layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))
        
        voltar_btn = Button(
            text='🔙',
            font_size=sp(24),
            size_hint_x=None,
            width=dp(60),
            background_color=get_color_from_hex('#95a5a6')
        )
        voltar_btn.bind(on_press=self.voltar)
        header.add_widget(voltar_btn)
        
        title = Label(
            text='⚙️ CONFIGURAÇÕES',
            font_size=sp(20),
            bold=True,
            color=get_color_from_hex('#f39c12')
        )
        header.add_widget(title)
        
        layout.add_widget(header)
        
        # Controle de volume
        volume_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60))
        
        volume_label = Label(
            text='🔊 Volume:',
            font_size=sp(16),
            size_hint_x=None,
            width=dp(100)
        )
        volume_layout.add_widget(volume_label)
        
        from kivy.uix.slider import Slider
        volume_slider = Slider(
            min=0,
            max=1,
            value=audio_manager.volume,
            step=0.1
        )
        volume_slider.bind(value=self.on_volume_change)
        volume_layout.add_widget(volume_slider)
        
        volume_value = Label(
            text=f'{int(audio_manager.volume * 100)}%',
            font_size=sp(16),
            size_hint_x=None,
            width=dp(60)
        )
        volume_layout.add_widget(volume_value)
        self.volume_value_label = volume_value
        
        layout.add_widget(volume_layout)
        
        # Informações do jogo
        info_layout = BoxLayout(orientation='vertical', spacing=dp(10))
        
        info_title = Label(
            text='📊 ESTATÍSTICAS',
            font_size=sp(18),
            bold=True,
            color=get_color_from_hex('#3498db'),
            size_hint_y=None,
            height=dp(40)
        )
        info_layout.add_widget(info_title)
        
        # Stats
        stats = [
            f"👤 Nome: {self.jogador['nome']}",
            f"🎯 Nível: {self.jogador['nivel']}",
            f"⭐ XP: {self.jogador['xp']}",
            f"💰 Ouro: {self.jogador['ouro']}",
            f"🐱 Mascotes: {len(self.jogador.get('mascotes', {}))}",
            f"🐎 Montarias: {len(self.jogador.get('montarias', {}))}"
        ]
        
        for stat in stats:
            stat_label = Label(
                text=stat,
                font_size=sp(14),
                color=get_color_from_hex('#bdc3c7'),
                size_hint_y=None,
                height=dp(30)
            )
            info_layout.add_widget(stat_label)
        
        layout.add_widget(info_layout)
        
        # Botões de ação
        actions_layout = BoxLayout(orientation='vertical', spacing=dp(10))
        
        reset_btn = Button(
            text='🔄 RESETAR PROGRESSO',
            font_size=sp(16),
            background_color=get_color_from_hex('#e74c3c'),
            size_hint_y=None,
            height=dp(50)
        )
        reset_btn.bind(on_press=self.confirmar_reset)
        actions_layout.add_widget(reset_btn)
        
        sobre_btn = Button(
            text='ℹ️ SOBRE O JOGO',
            font_size=sp(16),
            background_color=get_color_from_hex('#34495e'),
            size_hint_y=None,
            height=dp(50)
        )
        sobre_btn.bind(on_press=self.mostrar_sobre)
        actions_layout.add_widget(sobre_btn)
        
        layout.add_widget(actions_layout)
        
        self.add_widget(layout)
    
    def on_volume_change(self, instance, value):
        """Muda o volume"""
        audio_manager.set_volume(value)
        self.volume_value_label.text = f'{int(value * 100)}%'
        
        # Salvar configuração
        if "configuracoes" not in self.jogador:
            self.jogador["configuracoes"] = {}
        self.jogador["configuracoes"]["volume"] = value
        MobileDataManager.salvar_jogo(self.jogador)
    
    def confirmar_reset(self, instance):
        """Confirma reset do progresso"""
        content = BoxLayout(orientation='vertical', spacing=dp(15))
        
        warning_label = Label(
            text='⚠️ ATENÇÃO ⚠️\n\nIsto irá apagar TODO o seu progresso!\nEsta ação não pode ser desfeita.',
            font_size=sp(14),
            halign='center',
            color=get_color_from_hex('#e74c3c')
        )
        content.add_widget(warning_label)
        
        buttons_layout = BoxLayout(orientation='horizontal', spacing=dp(10))
        
        cancel_btn = Button(
            text='❌ CANCELAR',
            background_color=get_color_from_hex('#95a5a6'),
            size_hint_y=None,
            height=dp(40)
        )
        buttons_layout.add_widget(cancel_btn)
        
        confirm_btn = Button(
            text='🗑️ CONFIRMAR RESET',
            background_color=get_color_from_hex('#e74c3c'),
            size_hint_y=None,
            height=dp(40)
        )
        buttons_layout.add_widget(confirm_btn)
        
        content.add_widget(buttons_layout)
        
        popup = Popup(
            title='Confirmar Reset',
            content=content,
            size_hint=(0.9, 0.5)
        )
        
        cancel_btn.bind(on_press=popup.dismiss)
        confirm_btn.bind(on_press=lambda x: self.resetar_progresso(popup))
        
        popup.open()
    
    def resetar_progresso(self, popup):
        """Reseta o progresso do jogo"""
        popup.dismiss()
        
        # Apagar save
        try:
            save_file = os.path.join(MobileDataManager.get_save_path(), 'save_mobile.json')
            if os.path.exists(save_file):
                os.remove(save_file)
        except:
            pass
        
        # Recriar jogador padrão
        self.jogador = MobileDataManager.carregar_jogo()
        MobileDataManager.salvar_jogo(self.jogador)
        
        audio_manager.play_sound('success')
        self.mostrar_popup("Reset Completo!", "Seu progresso foi resetado com sucesso!")
    
    def mostrar_sobre(self, instance):
        """Mostra informações sobre o jogo"""
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        sobre_text = """🐲 RPG ÉPICO MOBILE 🦄

Versão: 1.0.0
Desenvolvido com Kivy

Um RPG épico com:
🐱 Sistema de Mascotes
🐎 Montarias Legendárias
⚔️ Equipamentos Poderosos
🏆 Conquistas Épicas

Criado para proporcionar uma experiência épica em dispositivos móveis!

© 2025 RPG Épico Mobile"""
        
        sobre_label = Label(
            text=sobre_text,
            font_size=sp(12),
            halign='center',
            valign='center'
        )
        content.add_widget(sobre_label)
        
        ok_btn = Button(
            text='OK',
            size_hint_y=None,
            height=dp(40),
            background_color=get_color_from_hex('#3498db')
        )
        content.add_widget(ok_btn)
        
        popup = Popup(
            title='Sobre o Jogo',
            content=content,
            size_hint=(0.9, 0.7)
        )
        
        ok_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def mostrar_popup(self, titulo, mensagem):
        """Mostra popup de mensagem"""
        content = BoxLayout(orientation='vertical', spacing=dp(10))
        
        label = Label(
            text=mensagem,
            font_size=sp(14),
            halign='center',
            valign='center'
        )
        content.add_widget(label)
        
        ok_btn = Button(
            text='OK',
            size_hint_y=None,
            height=dp(40),
            background_color=get_color_from_hex('#3498db')
        )
        content.add_widget(ok_btn)
        
        popup = Popup(
            title=titulo,
            content=content,
            size_hint=(0.8, 0.4)
        )
        
        ok_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def voltar(self, instance):
        """Volta ao menu principal"""
        audio_manager.play_sound('click')
        self.manager.current = 'menu'

class RPGEpicoApp(App):
    """Aplicação principal do RPG Épico Mobile"""
    
    def build(self):
        """Constrói a aplicação"""
        # Inicializar audio
        self.init_audio()
        
        # Screen Manager
        sm = ScreenManager()
        
        # Adicionar telas
        sm.add_widget(MenuPrincipalScreen(name='menu'))
        sm.add_widget(MascotesScreen(name='mascotes'))
        sm.add_widget(MontariasScreen(name='montarias'))
        sm.add_widget(ConfiguracoesScreen(name='configuracoes'))
        
        # Telas placeholder
        for screen_name in ['aventura', 'inventario', 'equipamentos', 'conquistas']:
            placeholder = Screen(name=screen_name)
            layout = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(20))
            
            title = Label(
                text=f'🚧 {screen_name.upper()} 🚧\nEm Desenvolvimento',
                font_size=sp(20),
                bold=True,
                halign='center'
            )
            layout.add_widget(title)
            
            voltar_btn = Button(
                text='🔙 VOLTAR',
                size_hint_y=None,
                height=dp(60),
                background_color=get_color_from_hex('#95a5a6')
            )
            voltar_btn.bind(on_press=lambda x: setattr(sm, 'current', 'menu'))
            layout.add_widget(voltar_btn)
            
            placeholder.add_widget(layout)
            sm.add_widget(placeholder)
        
        return sm
    
    def init_audio(self):
        """Inicializa sistema de áudio"""
        # Sons básicos (usar sons do sistema ou criar placeholders)
        sounds = {
            'click': None,
            'success': None,
            'error': None,
            'purchase': None
        }
        
        # Tentar carregar sons se existirem
        for sound_name in sounds:
            try:
                # Placeholder - em produção, usar arquivos de som reais
                pass
            except:
                pass

if __name__ == '__main__':
    RPGEpicoApp().run()

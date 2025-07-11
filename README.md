# RPG Épico Mobile - Versão Android APK

## 📱 Sobre o Projeto

Esta é a versão mobile do RPG Épico, otimizada para dispositivos Android. O jogo foi completamente reconstruído usando **Kivy** para proporcionar uma experiência nativa em smartphones e tablets.

## 🎮 Características Principais

### ✨ Sistemas Implementados
- 🐱 **Sistema de Mascotes Épicos** - 12+ criaturas lendárias
- 🐎 **Montarias Majestosas** - 6 tipos diferentes de montarias
- ⚙️ **Configurações Avançadas** - Controle de volume e estatísticas
- 💾 **Save System Mobile** - Compatível com armazenamento Android
- 🎵 **Audio Engine** - Sistema de som otimizado para mobile

### 🎨 Interface Mobile-First
- **Design Responsivo** - Adaptado para telas touch
- **Cards Visuais** - Interface moderna com gradientes
- **Navegação Intuitiva** - Botões grandes e fáceis de tocar
- **Scroll Suave** - Listas infinitas otimizadas
- **Popups Informativos** - Feedback visual completo

### 🚀 Performance Otimizada
- **Renderização Eficiente** - 60 FPS constantes
- **Baixo Consumo** - Otimizado para bateria
- **Carregamento Rápido** - Inicialização em segundos
- **Memória Controlada** - Gestão inteligente de recursos

## 📦 Como Gerar o APK

### Pré-requisitos
1. **Linux** (Ubuntu 20.04+ recomendado) ou **WSL no Windows**
2. **Python 3.8+**
3. **Java JDK 11**
4. **Android SDK**

### Instalação Rápida

```bash
# 1. Instalar dependências
sudo apt update
sudo apt install -y git zip unzip openjdk-11-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# 2. Instalar Buildozer
pip3 install --user buildozer

# 3. Clonar e preparar projeto
cd mobile_version/

# 4. Primeira compilação (instala dependências)
buildozer android debug

# 5. Gerar APK final
buildozer android release
```

### Compilação Detalhada

```bash
# Limpar cache (se necessário)
buildozer android clean

# Debug APK (para testes)
buildozer android debug

# Release APK (para distribuição)
buildozer android release

# APK será gerado em: bin/rpgepico-1.0.0-arm64-v8a-release.apk
```

## 📱 Instalação no Dispositivo

### Método 1: USB Debugging
```bash
# Conectar dispositivo via USB com depuração ativada
adb install bin/rpgepico-1.0.0-arm64-v8a-release.apk
```

### Método 2: Transferência Manual
1. Copie o arquivo `.apk` para o dispositivo
2. Abra o arquivo no celular
3. Permita "Instalar de fontes desconhecidas"
4. Toque em "Instalar"

### Método 3: Distribuição Online
- Upload para Google Play Store
- Distribuição via APKPure
- Hospedagem em servidor próprio

## 🎮 Como Jogar

### Controles Touch
- **Toque** - Selecionar/Ativar
- **Scroll** - Navegar por listas
- **Botão Voltar** - Retornar à tela anterior
- **Hold** - Informações detalhadas

### Primeiros Passos
1. **Inicie o jogo** - Toque no ícone
2. **Explore o Menu** - Navegue pelas opções
3. **Compre Mascotes** - Use suas 500 moedas iniciais
4. **Adquira Montarias** - Melhore sua velocidade
5. **Configure** - Ajuste volume e preferências

## 🗂️ Estrutura do Projeto

```
mobile_version/
├── main.py                 # Aplicação principal Kivy
├── buildozer.spec         # Configuração de build
├── README.md              # Este arquivo
├── requirements.txt       # Dependências Python
└── assets/               # Recursos do jogo
    ├── sounds/           # Arquivos de áudio
    ├── images/           # Imagens e ícones
    └── data/             # Dados do jogo
```

## 🛠️ Desenvolvimento

### Adicionar Novas Funcionalidades

```python
# 1. Criar nova Screen
class NovaScreen(Screen):
    def build_ui(self):
        # Implementar interface
        pass

# 2. Adicionar ao ScreenManager
sm.add_widget(NovaScreen(name='nova'))

# 3. Criar navegação
def ir_nova_tela(self, instance):
    self.manager.current = 'nova'
```

### Sistema de Save Personalizado

```python
# Salvar dados específicos
def salvar_progresso_customizado(dados):
    save_path = MobileDataManager.get_save_path()
    with open(f"{save_path}/custom_save.json", 'w') as f:
        json.dump(dados, f)
```

### Adicionar Sons

```python
# Carregar novo som
audio_manager.load_sound('novo_som', 'assets/sounds/novo.wav')

# Tocar som
audio_manager.play_sound('novo_som')
```

## 🎯 Sistemas Principais

### MascoteSystem
- **12 Mascotes Únicos** - Do comum ao mítico
- **Sistema de Raridade** - 6 níveis de poder
- **Compra/Ativação** - Gestão completa
- **Bônus Dinâmicos** - Poder baseado em nível

### MountSystem  
- **6 Montarias Épicas** - Terrestres, voadoras e mágicas
- **Velocidades Variadas** - 150 a 800 de velocidade
- **Sistema de Resistência** - Durabilidade realista
- **Ativação Exclusiva** - Uma montaria ativa por vez

### DataManager
- **Save Automático** - Persistência em tempo real
- **Compatibilidade Android** - Armazenamento externo
- **Backup Seguro** - Sistema à prova de falhas
- **Migração de Dados** - Atualização entre versões

## 🔧 Troubleshooting

### Erro na Compilação
```bash
# Limpar e recompilar
buildozer android clean
buildozer android debug
```

### APK não Instala
- Verificar se "Fontes desconhecidas" está habilitado
- Confirmar arquitetura compatível (ARM64/ARM32)
- Checar espaço disponível no dispositivo

### Jogo não Inicia
- Verificar logs: `adb logcat | grep python`
- Confirmar permissões de armazenamento
- Reinstalar aplicação

### Performance Baixa
- Fechar outros aplicativos
- Verificar versão Android (mínimo 5.0)
- Reiniciar dispositivo

## 📊 Especificações Técnicas

### Requisitos Mínimos
- **Android 5.0+** (API 21)
- **1GB RAM**
- **50MB armazenamento**
- **Processador ARMv7**

### Requisitos Recomendados
- **Android 8.0+** (API 26)
- **2GB RAM**
- **100MB armazenamento**
- **Processador ARM64**

### Compatibilidade
- ✅ Smartphones Android
- ✅ Tablets Android
- ✅ Chromebooks com suporte Android
- ❌ iOS (requer versão separada)

## 🚀 Próximas Atualizações

### Versão 1.1.0
- 🗺️ **Sistema de Aventuras** - Mapas exploráveis
- ⚔️ **Combate Dinâmico** - Batalhas em tempo real
- 🎒 **Inventário Completo** - 18 tipos de consumíveis
- 🏆 **Sistema de Conquistas** - 30+ achievements

### Versão 1.2.0
- 🌐 **Modo Online** - Multiplayer básico
- 📱 **Notificações Push** - Eventos do jogo
- 🎨 **Temas Personalizados** - 5 opções visuais
- 💰 **Sistema de Economia** - Loja expandida

### Versão 2.0.0
- 🏰 **Guildas** - Sistema social completo
- 🗺️ **Mundo Aberto** - Exploração livre
- ⚡ **Real-time PvP** - Batalhas entre jogadores
- 🎯 **Missões Diárias** - Conteúdo renovável

## 📝 Changelog

### v1.0.0 (Atual)
- ✨ Lançamento inicial
- 🐱 Sistema completo de mascotes
- 🐎 Sistema completo de montarias
- ⚙️ Configurações básicas
- 💾 Save system Android
- 🎵 Audio engine mobile

## 📄 Licença

Este projeto é um RPG épico desenvolvido para fins educacionais e de entretenimento. 

**Livre para uso pessoal** - Sinta-se à vontade para modificar e expandir o jogo!

---

## 💝 Agradecimentos

Desenvolvido com ❤️ usando:
- **Kivy** - Framework mobile Python
- **Buildozer** - Compilação APK
- **Android SDK** - Plataforma mobile
- **GitHub Copilot** - Assistência de desenvolvimento

**Transforme seu smartphone em uma arena épica! 🐲⚔️🦄**

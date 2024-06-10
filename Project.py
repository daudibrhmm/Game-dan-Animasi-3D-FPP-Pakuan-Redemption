from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

ujungkiri = -60
ujungkanan = 60
kecepatan = 8
kecepatan2 = 18

bullets = []
moving_targets = []

for i in range(9):
    x = random.randrange(15)
    y = random.randrange(1)
    z = random.randrange(15)
    moving_target = Entity(
        model='terorist.obj', 
        color=color.white,  
        scale=(1, 1, 0.1), 
        dx=0.05, 
        position=(x, y, z), 
        rotation_y=180,
        collider='mesh')
    moving_targets.append(moving_target)

def play_sound():
    sound = Audio('suaratembakan.mp3',autoplay=True)
    
def musik_kemenangan():
    sound = Audio('suarakemenangan.mp3',autoplay=True)
    
def start_music():
    music = Audio('backsound1.mp3', autoplay=True, loop=True)
    music.volume = 0.75
start_music()

try:
    def show_image():
        image_entity.texture = load_texture('tembakan') 
        image_entity.enabled = True
        time.sleep(2)  
        image_entity.enabled = False

    def on_left_click():
        show_image()

    image_entity = Entity(model='quad', texture=None, scale=(1.5, 1), enabled=False)
    
    if held_keys['Left down mouse']:
        on_left_click()

    print("Model tembakan berhasil dimuat.")
except Exception as e:
    print(f"Error loading gedung model: {e}")

gun = Entity(parent=camera, 
             model='Pistol1.glb', 
             color=color.brown,
             texture='silver', 
             origin_y=-0.5, 
             scale= (0.2,0.5,2), 
             position=(2,-1,2.5), 
             collider='box')

def destroy_bullet(bullet):
    if bullet in bullets:
        bullets.remove(bullet)
        destroy(bullet)

def input(key):
    global bullets
    if key == 'left mouse down':
        bullet = Entity(
            model='cube',
            scale=.1,
            position=(0.4, -0.4, 0.6),
            rotation_y=45,
            speed=20,
            color=color.brown,
            collider='box'
        )
        bullet.world_position = gun.world_position
        bullet.world_rotation = gun.world_rotation
        bullets.append(bullet)
        gun.blink(color.white)
        invoke(destroy_bullet, bullet, delay=3)
        play_sound()

sky = Sky(
    parent=scene,
    model='sphere',
    texture='night_sky_2',
    scale=500,
    double_sided=True
)

player_speed_normal = 4
player_speed_fast = 5
player_speed = player_speed_normal

player_start_position = Vec3(0, 5, 0)

def check_player_position():
    global player
    if player.Z < -15:  
        player.position = player_start_position

try:
    gedung_model = Entity(
        model="gedung2.obj", 
        texture='solid',
        scale=(0.4, 0.5, 0.6),
        position=(20, 0.01, 10),
        collider='mesh'
    )
    print("Model gedung berhasil dimuat.")
except Exception as e:
    print(f"Error loading gedung model: {e}")
    
       
orangkampus1 = Entity (
        model="orangkampus1.obj",
        scale=(1, 1.3, 0.9),
        position=(25, 0, 10),
        rotation_y=-90,
        collider='box'
    )  

try:
    meja_model = Entity (
        model="mejo.glb",
        texture='solid',
        scale=(0.8, 0.4, 0.7),
        position=(45, 0, 18),
        rotation_y=180,
        collider='box'
    )   
    print("Model meja berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")
    
try:    
    orangkampus = Entity (
        model="orangkampus.obj",
        scale=(1, 1.3, 0.9),
        position=(33, 0, 38),
        rotation_y=180,
        collider='box'
    )  
    
    print("Model orang berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}") 

try:
    pohon_model = Entity (
        model="lowpoly_tree_sample.obj",
        texture='solid',
        scale=(0.7, 0.7, 0.7),
        position=(38, 0, 32),
        collider='box'
    )   
    print("Model pohon 1 berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")

try:
    pohon2_model = Entity (
        model="pohon.glb",
        texture='solid',
        scale=(1, 2, 1),
        position=(35, 0, -22),
        collider='box'
    )   
    print("Model pohon 2 berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")

try:
    gedungrektor_model = Entity (
        model="building.glb",
        texture='solid',
        scale=(10, 10, 9),
        position=(40, 0, -37),
        rotation_y=90,
        collider='box'
    )   
    print("Model Large Building berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")
    

try:
    mobilpolisi_model = Entity (
        model="mobil polisi.glb",
        texture='solid',
        scale=(0.7, 0.7, 0.7),
        position=(-57, -0.07, -20),
        collider='mesh'
    )   
    mobilpolisi2 = duplicate(mobilpolisi_model, x=-40, z=-30)
    mobilpolisi3 = duplicate(mobilpolisi2, x=-20)
    
    print("Model mobil polisi berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")

try:
    gedung4_model = Entity (
        model="gedung4.obj",
        texture='solid',
        scale=(1.5, 2, 1.5),
        position=(50, -2, -20),
        collider='box'
    )   
    print("Model Gedung 4 berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")
    
try:
    gedungrektorat_model = Entity (
        model="gedungrektorat.obj",
        texture='solid',
        scale=(7, 8, 5),
        position=(-37, 0, 26),
        rotation_y=90,
        collider='box'
    )   
    
    print("Model Gedung rektorat berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")


try:
    soldiers = Entity (
        model="soldiers.obj",
        texture='none',
        scale=(0.2, 0.2, 0.2),
        position=(-28, 0, -75),
        collider='mesh',
        rotation_y=45
    )   
    soldiers2 = duplicate(soldiers, x=-5, z=-68, rotation_y=0)
    soldiers3 = duplicate(soldiers, x=-20, rotation_y=0)
    
    print("Model police line berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")
    
try:
    barier = Entity (
        model="barier.obj",
        texture='none',
        scale=(2, 2, 1),
        position=(7, 0, 5),
        collider='mesh',
        rotation_y=180,
    )   
    barier2 = duplicate(barier, x=9, z=25)
    barier3 = duplicate(barier,x=-10, z=11,)
    barier4= duplicate(barier,x=-1, z=-2)
    print("Model barier berhasil dimuat.")
except Exception as e:
    print(f"Error loading barier model: {e}")

try:
    policeline_model = Entity (
        model="policeline.obj",
        texture='none',
        scale=(0.8, 0.8, 0.8),
        position=(-28, 0, -70),
        collider='mesh'
    )   
    policeline2 = duplicate(policeline_model, x=-10)
    policeline3 = duplicate(policeline2, x=8)
    print("Model police line berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")

try:
    lapanganbasket_model = Entity (
        model="lapanganbasket.glb",
        texture='none',
        scale=(1.5, 2, 1.2),
        position=(2, 0, 35),
        rotation_y=90,
        collider='mesh'
    )   
    print("Model lapangan Basket berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")

try:
    Gedung2_model = Entity (
        model="gedung3.obj",
        texture='none',
        scale=(0.5, 0.5, 0.5),
        position=(-38, 0, -20),
        rotation_y=180,
        collider='mesh'
    )   
    print("Model Gedung 2 berhasil dimuat.")
except Exception as e:
    print(f"Error loading pohon model: {e}")

car_model = Entity (
        model="car.obj",
        texture='none',
        scale=(0.6, 0.7, 0.5),
        position=(35, 0, -58),
        collider='None'
    )   
car1 = duplicate(car_model,x=39),
car2 = duplicate(car_model, x=31),

cardodge_model = Entity (
        model="cardodge.obj",
        texture='none',
        scale=(0.6, 0.7, 0.5),
        position=(28, 0, -55),
        collider='None'
    )   
cardodge1 = duplicate(cardodge_model,x=25),
cardodge2 = duplicate(cardodge_model, x=22),

road = Entity (
        model="jalanbesar.obj",
        texture='none',
        scale=(2.5, 1, 1),
        position=(1, 0, -125),
        collider='mesh'
    ) 

        
ground = Entity(
    model='plane',
    texture='rumput',
    scale=(100, 1, 250),
    texture_scale=(200, 200),
    collider='box'
)

billboard = Entity(
    model="billboard.obj",  
    color=color.white,  
    scale=(0.5, 0.7, 0.3),
    position=(-47, 0, -110),
    rotation_y=90,
    collider='box'  
)

billboard2 = Entity(
    model="billboard2.obj",  
    color=color.white,  
    scale=(0.4, 0.5, 0.3),
    position=(-47, 0, -75),
    rotation_y=90,
    collider='box'  
)

pohongede =Entity(
    model="pohongede.obj",  
    color=color.white,  
    scale=(0.1, 0.2, 0.2),
    position=(40, -3, -110),
    rotation_y=-90,
    collider='None'  
)

pohongede1 = duplicate(pohongede,x=30)
pohongede2 = duplicate(pohongede, x=20)

bangunanluar =Entity(
    model="bangunanluar.obj",  
    color=color.white,  
    scale=(0.3, 0.2, 0.2),
    position=(30, -1, -90),
    rotation_y=-90,
    collider='None'  
)

orangdihalte = Entity(
    model="orangdihalte.obj",  
    color=color.white,  
    scale=(0.3, 0.2, 0.2),
    position=(-35, 0, -110),
    rotation_y=180,
    collider='mesh'  
)

stop = Entity(
    model="stop.obj",  
    color=color.white,  
    scale=(0.5, 0.7, 0.4),
    position=(-32, -2, -110),
    rotation_y=90,
    collider='mesh'  
)

mobilninut = Entity(
    model="mobilpolisi.obj",  
    color=color.white,  
    scale=(0.8, 1, 0.5),
    position=(-50, 0, -122),
    rotation_y=90,
    collider='box'  
)

mobilkencang =Entity(
    model="mobilkencang.obj",  
    color=color.white,  
    scale=(0.5, 0.5, 0.4),
    position=(50, 0, -128),
    rotation_y=-90,
    collider='None'  
)

wall = Entity(
    model='cube',
    texture='wall',
    collider='cube',
    scale=(35, 10, 5),
    position=(35, 5, -50),
    color=color.gray
)



wall1 = Entity(
    model='cube',
    texture='wall',
    collider='cube',
    scale=(100, 10, 5),
    position=(0, 5, 50),
    color=color.gray
)

wall3 = duplicate(wall1, rotation_y=90, x=-50, z=0)
wall4 = duplicate(wall3, x=50)
wall5 = duplicate(wall1, x=-35)

def update():
    
    mobilkencang.x -= time.dt * kecepatan2
    if mobilkencang.x < ujungkiri:
        mobilkencang.x = ujungkanan
    
    
    mobilninut.x += time.dt * kecepatan
    if mobilninut.x > ujungkanan:
        mobilninut.x = ujungkiri
        
    global bullets
    for m in moving_targets:
        m.x += m.dx
        if m.x > 9:
            m.x = 9
            m.dx *= -1
        if m.x < -9:
            m.x = -9
            m.dx *= -1

    if len(bullets) > 0:
        for b in bullets:
            b.position += b.forward * 8
            hit_info = b.intersects()
            if hit_info.hit:
                for m in moving_targets:
                    if hit_info.entity == m:
                        moving_targets.remove(m)
                        destroy(m)
                        break  
                if len(moving_targets) == 0:
                      message = Text(text = 'Kamu Membebaskan Universitas!', scale=2, origin=(0,0), background=True, color=color.green)
                      musik_kemenangan()
                      
if held_keys['escape']:  
        application.quit()

player = FirstPersonController(model='cube', y=0, origin_y=-.5)

window.fullscreen = False
window.fps_counter.enabled = True
window.exit_button.visible = True
window.title = 'Ursina 3D Model Example'

app.run()

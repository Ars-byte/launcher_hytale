import customtkinter as ctk
import subprocess
import os
import sys
import time
import platform
import webbrowser
import re
from PIL import Image

ctk.set_appearance_mode("Dark")

class HytaleLauncher(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.base_path = os.path.dirname(os.path.realpath(__file__))
        self.script_name = "hytale.sh"
        self.github_url = "https://github.com/Ars-byte"
        self.required_libs = ["libpng", "libSDL2"]
        
        self.current_lang = "es"
        self.texts = {
            "es": {
                "title": "Hytale Launcher",
                "github": "mi perfil de github: github.com/Ars-byte",
                "nickname": "Nombre de usuario:",
                "launch": "Lanzar Aplicación",
                "running": "EJECUTANDO...",
                "checking_notice": "se verificaran las librerias necesarias para jugar hytale",
                "checking": "Verificando librerías...",
                "libs_ok": "librerias requeridas instaladas",
                "libs_fail": "Aviso: {} no detectadas",
                "start": "Iniciando {}...",
                "success": "Hytale lanzado con éxito",
                "error_file": "CRITICAL: '{}' no encontrado",
                "lang_btn": "English"
            },
            "en": {
                "title": "Hytale Launcher",
                "github": "my github profile: github.com/Ars-byte",
                "nickname": "Username:",
                "launch": "Launch Application",
                "running": "RUNNING...",
                "checking_notice": "the necessary libraries to play hytale will be verified",
                "checking": "Checking libraries...",
                "libs_ok": "required libraries installed",
                "libs_fail": "Warning: {} not detected",
                "start": "Starting {}...",
                "success": "Hytale launched successfully",
                "error_file": "CRITICAL: '{}' not found",
                "lang_btn": "Español"
            }
        }

        self.os_info = platform.system().lower()
        self.kernel_info = platform.version() if platform.system() == "Windows" else platform.release()
        self.cpu_info = self.get_cpu_info()
        self.gpu_info = self.get_gpu_info()

        self.title("Hytale Launcher")
        self.geometry("550x600")
        self.resizable(False, False)
        self.configure(fg_color="#000000")

        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.pack(pady=(30, 10), padx=30, fill="x")

        img_path = os.path.join(self.base_path, "assets", "github_avatar.png")
        if os.path.exists(img_path):
            my_image = ctk.CTkImage(light_image=Image.open(img_path),
                                    dark_image=Image.open(img_path),
                                    size=(60, 60))
            self.profile_pic = ctk.CTkLabel(self.header_frame, image=my_image, text="")
            self.profile_pic.pack(side="left", padx=(0, 15))
        
        self.title_container = ctk.CTkFrame(self.header_frame, fg_color="transparent")
        self.title_container.pack(side="left", fill="y")

        self.title_label = ctk.CTkLabel(self.title_container, text=self.texts[self.current_lang]["title"], font=("Inter", 24, "bold"), text_color="#ffffff")
        self.title_label.pack(anchor="w")

        self.link_label = ctk.CTkLabel(self.title_container, text=self.texts[self.current_lang]["github"], font=("Inter", 11), text_color="#666666", cursor="hand2")
        self.link_label.pack(anchor="w")
        self.link_label.bind("<Button-1>", lambda e: webbrowser.open(self.github_url))
        self.nick_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.nick_frame.pack(fill="x", padx=30, pady=(10, 5))
        self.nick_label = ctk.CTkLabel(self.nick_frame, text=self.texts[self.current_lang]["nickname"], font=("Inter", 12, "bold"), text_color="#ffffff")
        self.nick_label.pack(side="left", padx=(0, 10))
        self.nick_entry = ctk.CTkEntry(self.nick_frame, placeholder_text="Nickname", fg_color="#121212", border_color="#252525", text_color="#ffffff", corner_radius=8, height=35)
        self.nick_entry.pack(side="left", expand=True, fill="x")
        self.nick_entry.insert(0, "Ars")
        self.info_box = ctk.CTkTextbox(self, fg_color="#121212", text_color="#a0a0a0", border_color="#252525", border_width=1, corner_radius=15, font=("Monospace", 11), padx=20, pady=20)
        self.info_box.pack(expand=True, fill="both", padx=30, pady=(10, 20))
        self.refresh_sys_info()
        self.lang_btn = ctk.CTkButton(self, text=self.texts[self.current_lang]["lang_btn"], command=self.toggle_language, fg_color="#1a1a1a", text_color="#ffffff", hover_color="#252525", font=("Inter", 11), corner_radius=8, height=25, width=80)
        self.lang_btn.pack(pady=(0, 10))
        self.launch_btn = ctk.CTkButton(self, text=self.texts[self.current_lang]["launch"], command=self.launch, fg_color="#ffffff", text_color="#000000", hover_color="#d1d1d1", font=("Inter", 14, "bold"), corner_radius=12, height=50)
        self.launch_btn.pack(pady=(0, 30), padx=30, fill="x")

    def refresh_sys_info(self):
        self.info_box.configure(state="normal")
        self.info_box.delete("1.0", "end")
        self.info_box.insert("0.0", f"system: {self.os_info}\n")
        self.info_box.insert("end", f"kernel: {self.kernel_info}\n")
        self.info_box.insert("end", f"cpu:    {self.cpu_info}\n")
        self.info_box.insert("end", f"gpu:    {self.gpu_info}\n")
        self.info_box.insert("end", "—" * 30 + "\n")
        self.info_box.configure(state="disabled")

    def toggle_language(self):
        self.current_lang = "en" if self.current_lang == "es" else "es"
        self.title_label.configure(text=self.texts[self.current_lang]["title"])
        self.link_label.configure(text=self.texts[self.current_lang]["github"])
        self.nick_label.configure(text=self.texts[self.current_lang]["nickname"])
        self.launch_btn.configure(text=self.texts[self.current_lang]["launch"])
        self.lang_btn.configure(text=self.texts[self.current_lang]["lang_btn"])

    def get_cpu_info(self):
        try:
            if platform.system() == "Windows": return platform.processor()
            return subprocess.check_output("grep -m 1 'model name' /proc/cpuinfo | cut -d: -f2", shell=True).decode().strip()
        except: return "Generic CPU"

    def get_gpu_info(self):
        try:
            if platform.system() == "Windows":
                cmd = "wmic path win32_VideoController get name"
                return subprocess.check_output(cmd, shell=True).decode().split("\n")[1].strip()
            gpu_data = subprocess.check_output("lspci | grep -E 'VGA|3D'", shell=True).decode().strip()
            return gpu_data.split(": ")[-1] if ":" in gpu_data else gpu_data
        except: return "Unknown GPU"

    def update_username_in_sh(self, script_path, new_name):
        try:
            with open(script_path, 'r') as f:
                content = f.read()

            new_content = re.sub(r'^username=.*', f'username={new_name}', content, flags=re.MULTILINE)
            
            with open(script_path, 'w') as f:
                f.write(new_content)
            return True
        except Exception as e:
            self.write_log(f"Error actualizando nickname: {e}")
            return False

    def check_dependencies(self):
        if platform.system() == "Windows": return True
        self.write_log(self.texts[self.current_lang]["checking_notice"])
        time.sleep(0.5)
        missing = []
        for lib in self.required_libs:
            try:
                subprocess.check_output(f"ldconfig -p | grep -i {lib}", shell=True, stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError:
                missing.append(lib)
        if not missing:
            self.write_log(self.texts[self.current_lang]["libs_ok"])
            return True
        else:
            self.write_log(self.texts[self.current_lang]["libs_fail"].format(", ".join(missing)))
            return False

    def write_log(self, text):
        self.info_box.configure(state="normal")
        self.info_box.insert("end", f"> {text}\n")
        self.info_box.see("end")
        self.info_box.configure(state="disabled")
        self.update()

    def launch(self):
        script_path = os.path.join(self.base_path, self.script_name)
        if os.path.exists(script_path):
            self.launch_btn.configure(state="disabled", text=self.texts[self.current_lang]["running"])

            chosen_nick = self.nick_entry.get().strip() or "Ars"
            if self.update_username_in_sh(script_path, chosen_nick):
                self.write_log(f"Nickname actualizado a: {chosen_nick}")
            
            self.check_dependencies()
            self.write_log(self.texts[self.current_lang]["start"].format(self.script_name))
            
            if platform.system() != "Windows":
                try: subprocess.run(["chmod", "+x", script_path], check=True)
                except: pass
            try:
                subprocess.Popen(["/bin/bash", script_path], cwd=self.base_path)
                self.write_log(self.texts[self.current_lang]["success"])
                self.after(3000, self.destroy)
            except Exception as e:
                self.write_log(f"ERROR: {str(e)}")
                self.launch_btn.configure(state="normal", text=self.texts[self.current_lang]["launch"])
        else:
            self.write_log(self.texts[self.current_lang]["error_file"].format(self.script_name))
            self.launch_btn.configure(state="normal", text=self.texts[self.current_lang]["launch"])

if __name__ == "__main__":
    app = HytaleLauncher()
    app.mainloop()
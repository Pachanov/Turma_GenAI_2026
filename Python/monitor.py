import time
from datetime import datetime

class LoginMonitor:
    def __init__(self):
        self.logged_in = False
        self.login_time = None
        self.logout_time = None
        self.total_logged_time = 0
        self.total_logout_time = 0
        self.sessions = []

    def login(self):
        if not self.logged_in:
            self.login_time = datetime.now()
            self.logged_in = True
            if self.logout_time:
                logout_duration = (self.login_time - self.logout_time).total_seconds()
                self.total_logout_time += logout_duration
            print(f"✓ Login em: {self.login_time.strftime('%H:%M:%S')}")
        else:
            print("Já está logado!")

    def logout(self):
        if self.logged_in:
            self.logout_time = datetime.now()
            self.logged_in = False
            logged_duration = (self.logout_time - self.login_time).total_seconds()
            self.total_logged_time += logged_duration
            self.sessions.append({
                'login': self.login_time,
                'logout': self.logout_time,
                'duration': logged_duration
            })
            print(f"✗ Logout em: {self.logout_time.strftime('%H:%M:%S')}")
            print(f"Tempo logado: {logged_duration:.2f}s")
        else:
            print("Não está logado!")

    def status(self):
        status_str = "Logado" if self.logged_in else "Deslogado"
        print(f"\nStatus: {status_str}")
        print(f"Total de tempo logado: {self.total_logged_time:.2f}s")
        print(f"Total de tempo deslogado: {self.total_logout_time:.2f}s")
        print(f"Sessões: {len(self.sessions)}\n")

    def report(self):
        print("\n=== Relatório de Sessões ===")
        for i, session in enumerate(self.sessions, 1):
            print(f"Sessão {i}: {session['duration']:.2f}s")


if __name__ == "__main__":
    monitor = LoginMonitor()
    
    monitor.login()
    time.sleep(2)
    monitor.logout()
    
    monitor.login()
    time.sleep(3)
    monitor.logout()
    
    monitor.status()
    monitor.report()
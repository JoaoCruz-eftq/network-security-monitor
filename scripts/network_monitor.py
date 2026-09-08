from collections import Counter
from pathlib import Path

LOG_FILE = Path(__file__).parent.parent / "logs" / "security.log"

SUSPICIOUS_EVENTS = {
    "LOGIN_FAILED",
    "CONNECTION_DENIED",
    "PORT_SCAN"
}

ALERT_THRESHOLD = 3


def read_logs():
    """Lê os eventos registrados no arquivo de log."""
    if not LOG_FILE.exists():
        print("Arquivo de log não encontrado.")
        return []

    events = []

    with open(LOG_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = [item.strip() for item in line.split("|")]

            if len(parts) != 3:
                continue

            timestamp, ip, event = parts

            events.append({
                "timestamp": timestamp,
                "ip": ip,
                "event": event
            })

    return events


def analyze_events(events):
    """Analisa eventos suspeitos agrupando-os por endereço IP."""
    suspicious_ips = Counter()

    for event in events:
        if event["event"] in SUSPICIOUS_EVENTS:
            suspicious_ips[event["ip"]] += 1

    return suspicious_ips


def generate_report(events, suspicious_ips):
    """Exibe o resultado da análise."""
    print("=" * 55)
    print("NETWORK SECURITY MONITOR")
    print("=" * 55)

    print(f"\nTotal de eventos analisados: {len(events)}")

    print("\nEventos suspeitos por IP:")

    if not suspicious_ips:
        print("Nenhuma atividade suspeita encontrada.")
        return

    for ip, count in suspicious_ips.items():
        if count >= ALERT_THRESHOLD:
            print(
                f"[ALERTA] IP {ip} apresentou "
                f"{count} eventos suspeitos."
            )
        else:
            print(
                f"[INFO] IP {ip}: "
                f"{count} eventos suspeitos."
            )


def main():
    events = read_logs()
    suspicious_ips = analyze_events(events)
    generate_report(events, suspicious_ips)


if __name__ == "__main__":
    main()

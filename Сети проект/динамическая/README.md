## Что было сделано

### 1. Настройка IP-адресации на интерфейсах

**R1 (FastEthernet0/0 и FastEthernet0/1):**
команды:
```cisco
	interface FastEthernet0/0
	ip address 10.0.12.1 255.255.255.0

	interface FastEthernet0/1
	ip address 192.168.1.1 255.255.255.0
```

**R2 (FastEthernet0/0 и FastEthernet0/1):**

команды:
```cisco
	interface FastEthernet0/0
	ip address 10.0.12.2 255.255.255.0

	interface FastEthernet0/1
	ip address 10.0.23.2 255.255.255.0
```

**R3 (FastEthernet0/0 и FastEthernet0/1):**

команды:
```cisco
	interface FastEthernet0/0
	ip address 10.0.23.3 255.255.255.0

	interface FastEthernet0/1
	ip address 192.168.3.1 255.255.255.0
```

### 2. Настройка OSPF

На всех трёх маршрутизаторах объявлены сети в Area 0:

**R1:**
**команды:**
```cisco
	router ospf 1
	network 10.0.12.0 0.0.0.255 area 0
	network 192.168.1.0 0.0.0.255 area 0
```

**R2:**
**команды:**
```cisco
	router ospf 1
	network 10.0.12.0 0.0.0.255 area 0
	network 10.0.23.0 0.0.0.255 area 0

```

**R3:**
**команды:**
```cisco
	router ospf 1
	network 10.0.23.0 0.0.0.255 area 0
	network 192.168.3.0 0.0.0.255 area 0
```


## Результат: соседство OSPF установлено (FULL/DR)

**R1 видит соседа R2:**
**команды:**

	show ip ospf neighbor
	
Neighbor ID Pri State Dead Time Address Interface
10.0.23.2 1 FULL/BDR 00:00:37 10.0.12.2 FastEthernet0/0



**R2 видит обоих соседей (R1 и R3):**
**команды:**

	show ip ospf neighbor
	
Neighbor ID Pri State Dead Time Address Interface
192.168.3.1 1 FULL/DR 00:00:31 10.0.23.3 FastEthernet0/1
192.168.1.1 1 FULL/DR 00:00:31 10.0.12.1 FastEthernet0/0

text

**R3 видит соседа R2:**
**команды:**

	show ip ospf neighbor
	
Neighbor ID  | Pri  | State Dead    |  Time     | Address     |  Interface
10.0.23.2    | 1    |   FULL/BDR    | 00:00:35  | 10.0.23.2   |  FastEthernet0/0


## Проверка связности

После настройки OSPF маршрутизаторы автоматически обменялись маршрутами. R1 знает о сети 192.168.3.0/24, а R3 знает о сети 192.168.1.0/24.

**Пинг с R1 на 192.168.3.1** (интерфейс R3) — успешен
**Пинг с R3 на 192.168.1.1** (интерфейс R1) — успешен

*Таблица маршрутизации на R1 показывает, что маршрут до 192.168.3.0/24 получен через OSPF от R2.*

## Использованные технологии
`GNS3`, `Cisco IOS (3745)`, `OSPF (Area 0)`, `IP-адресация`, `CLI`

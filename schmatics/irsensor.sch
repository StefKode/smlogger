EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:switches
LIBS:relays
LIBS:motors
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:irsensor-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Q_NPN_BCE Q1
U 1 1 5DDD8127
P 4100 2600
F 0 "Q1" H 4300 2650 50  0000 L CNN
F 1 "NPN" H 4300 2550 50  0000 L CNN
F 2 "" H 4300 2700 50  0001 C CNN
F 3 "" H 4100 2600 50  0001 C CNN
	1    4100 2600
	1    0    0    -1  
$EndComp
$Comp
L Q_NPN_BCE Q2
U 1 1 5DDD81FA
P 4950 2600
F 0 "Q2" H 5150 2650 50  0000 L CNN
F 1 "NPN" H 5150 2550 50  0000 L CNN
F 2 "" H 5150 2700 50  0001 C CNN
F 3 "" H 4950 2600 50  0001 C CNN
	1    4950 2600
	1    0    0    -1  
$EndComp
$Comp
L R R3
U 1 1 5DDD85C1
P 4200 2100
F 0 "R3" V 4280 2100 50  0000 C CNN
F 1 "22k" V 4200 2100 50  0000 C CNN
F 2 "" V 4130 2100 50  0001 C CNN
F 3 "" H 4200 2100 50  0001 C CNN
	1    4200 2100
	1    0    0    -1  
$EndComp
$Comp
L R R4
U 1 1 5DDD8917
P 5050 2100
F 0 "R4" V 5130 2100 50  0000 C CNN
F 1 "2.2k" V 5050 2100 50  0000 C CNN
F 2 "" V 4980 2100 50  0001 C CNN
F 3 "" H 5050 2100 50  0001 C CNN
	1    5050 2100
	1    0    0    -1  
$EndComp
$Comp
L R_Variable R1
U 1 1 5DDD9756
P 3600 2100
F 0 "R1" V 3700 2000 50  0000 L CNN
F 1 "22k" V 3500 2050 50  0000 L CNN
F 2 "" V 3530 2100 50  0001 C CNN
F 3 "" H 3600 2100 50  0001 C CNN
	1    3600 2100
	1    0    0    -1  
$EndComp
$Comp
L R_Variable R2
U 1 1 5DDD9BB8
P 3600 2900
F 0 "R2" V 3700 2800 50  0000 L CNN
F 1 "22k" V 3500 2850 50  0000 L CNN
F 2 "" V 3530 2900 50  0001 C CNN
F 3 "" H 3600 2900 50  0001 C CNN
	1    3600 2900
	1    0    0    -1  
$EndComp
$Comp
L R R5
U 1 1 5DDDA555
P 5350 2350
F 0 "R5" V 5430 2350 50  0000 C CNN
F 1 "2.2k" V 5350 2350 50  0000 C CNN
F 2 "" V 5280 2350 50  0001 C CNN
F 3 "" H 5350 2350 50  0001 C CNN
	1    5350 2350
	0    1    1    0   
$EndComp
$Comp
L R R6
U 1 1 5DDDA8B2
P 5650 2600
F 0 "R6" V 5730 2600 50  0000 C CNN
F 1 "1k" V 5650 2600 50  0000 C CNN
F 2 "" V 5580 2600 50  0001 C CNN
F 3 "" H 5650 2600 50  0001 C CNN
	1    5650 2600
	1    0    0    -1  
$EndComp
$Comp
L R R7
U 1 1 5DDDACA1
P 6000 2600
F 0 "R7" V 6080 2600 50  0000 C CNN
F 1 "1k" V 6000 2600 50  0000 C CNN
F 2 "" V 5930 2600 50  0001 C CNN
F 3 "" H 6000 2600 50  0001 C CNN
	1    6000 2600
	1    0    0    -1  
$EndComp
$Comp
L C_Small C1
U 1 1 5DDDB987
P 4600 2900
F 0 "C1" H 4610 2970 50  0000 L CNN
F 1 "100pf" H 4610 2820 50  0000 L CNN
F 2 "" H 4600 2900 50  0001 C CNN
F 3 "" H 4600 2900 50  0001 C CNN
	1    4600 2900
	1    0    0    -1  
$EndComp
Wire Wire Line
	3600 2250 3600 2750
Wire Wire Line
	5050 2250 5050 2400
Wire Wire Line
	4600 2350 4600 2800
Connection ~ 4600 2600
Wire Wire Line
	4200 2250 4200 2400
Wire Wire Line
	4600 2600 4750 2600
Wire Wire Line
	4600 2350 4200 2350
Connection ~ 4200 2350
Wire Wire Line
	3200 3150 6150 3150
Wire Wire Line
	4200 3150 4200 2800
Wire Wire Line
	4600 3150 4600 3000
Wire Wire Line
	5050 3150 5050 2800
Connection ~ 4600 3150
Wire Wire Line
	3200 2600 3900 2600
Connection ~ 3600 2600
Wire Wire Line
	4050 1850 6150 1850
Wire Wire Line
	4200 1850 4200 1950
Wire Wire Line
	5050 1850 5050 1950
Connection ~ 4200 1850
$Comp
L D_Photo D1
U 1 1 5DDF6E07
P 3200 2950
F 0 "D1" H 3220 3020 50  0000 L CNN
F 1 "photodiode" H 3160 2840 50  0000 C CNN
F 2 "" H 3150 2950 50  0001 C CNN
F 3 "" H 3150 2950 50  0001 C CNN
	1    3200 2950
	0    1    1    0   
$EndComp
Wire Wire Line
	3200 2600 3200 2750
Wire Wire Line
	5200 2350 5050 2350
Connection ~ 5050 2350
Wire Wire Line
	5500 2350 5650 2350
Wire Wire Line
	5650 2350 5650 2450
Wire Wire Line
	5650 2750 5650 2850
Wire Wire Line
	5650 2850 6000 2850
Wire Wire Line
	6000 2850 6000 2750
Wire Wire Line
	6000 2450 6000 2350
Text GLabel 6150 2350 2    60   Output ~ 0
RPI-Z_GPIO_RX
Wire Wire Line
	6000 2350 6150 2350
Text GLabel 6150 3150 2    60   UnSpc ~ 0
RPI-Z_GND
Text GLabel 6150 1850 2    60   UnSpc ~ 0
RPI-Z_5V
Wire Wire Line
	3600 1850 3600 1950
Wire Wire Line
	3200 3050 3200 3150
Wire Wire Line
	3600 3150 3600 3050
Connection ~ 4200 3150
Connection ~ 3600 3150
Connection ~ 5050 3150
Connection ~ 5050 1850
Text Notes 5550 2200 0    60   ~ 0
Output does not exceed 3.3V
$Comp
L R R8
U 1 1 5E05F263
P 3900 1850
F 0 "R8" V 3980 1850 50  0000 C CNN
F 1 "1k" V 3900 1850 50  0000 C CNN
F 2 "" V 3830 1850 50  0001 C CNN
F 3 "" H 3900 1850 50  0001 C CNN
	1    3900 1850
	0    1    1    0   
$EndComp
Wire Wire Line
	3600 1850 3750 1850
$EndSCHEMATC

class MedidaInvalidaError(Exception):
    '''Medida Invalida'''

import os
import sys
import csv

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def general_data_cleaner(archivo_base, archivo_voip, archivo_speed, archivo_info):

    with open (archivo_base, 'r',encoding='utf-8') as archivo_base, open (archivo_voip, 'w',newline='',encoding='utf-8') as voip, open (archivo_speed, 'w',newline='',encoding='utf-8') as speed, open (archivo_info, 'w', encoding='utf-8') as archivo_info:
        reader = csv.DictReader(archivo_base, delimiter=',')
        # fieldnames_for_voip = []
        # fieldnames_for_speed = []
        # fieldnames_unused = ['Local Time', 'Test Duration (min/sec)', 'Test Outcome', 'Fail Reason', 'Target Calls', 'Supported Calls', 'Download Speed (Mbps)', 'Upload Speed (Mbps)', 'Upstream Jitter (ms)', 'Downstream Jitter (ms)', 'Upstream Packet Loss (%)', 'Downstream Packet Loss (%)', 'SIP ALG', 'Round Trip Time (ms)', 'Blocked Ports', 'Error source', 'Error type', 'Error id', 'Id error code', 'Error description', 'Latency', 'Failure', 'Method', 'kB Read', 'kB Write', 'Kbps Read', 'Kbps Write', 'RTTMin', 'RTTAvg', 'RTTMax', 'D/load capacity (Kbps)', 'U/load capacity (Kbps)', 'D/load packets', 'U/load packets', 'Packet size', 'QOS', 'D/load max limit (Kbps)', 'U/load max limit (Kbps)', 'Errors', 'IP Available', 'Subnet Mask (1)', 'Time Offset (2)', 'Gateway IP (3)', 'DNS IP(s)(6)', 'NTP Servers (42)', 'Server ID (54)', 'Server Name (66)', 'VLAN ID (132)', 'TFTP ethBoot and GRUB (150)', 'v4 Port Params (159)', 'Captive Portal (160)', 'Options Requested', 'Download speed', 'Upload speed', 'D/load COS', 'U/load COS', 'Min RTT', 'Max RTT', 'Avg RTT', 'RTT Consistency', 'Max Delay', 'Avg Delay', 'Effective speed', 'Route Speed', 'Forced Idle', 'Route Conc', 'Download test', 'Upload test', 'Errors', 'Avg Response', 'Min Response', 'Max Response', 'Port \#', 'Protocol', 'Ports Open', 'Ports Blocked', 'Total Ports Open', 'Total Ports Blocked', 'Ports Blocked List', 'Max delay variance', 'Avg delay variance', 'Consistency of service', 'Lost packets', 'Percent lost', 'Contiguous loss', 'Loss distribution', 'Loss distribution %', 'Pkts out of order', '% out of order', 'Echoed packets', 'Echo %', 'Agg max delay variance', 'Agg max COS', 'Agg min COS', 'Agg lost packets', 'Percent lost', 'Agg contiguous lost packets', 'Agg loss distribution', 'Agg loss distribution %', 'Agg pkts out of order', 'Agg % out of order', 'Agg echoed packets', 'Agg echo %', 'Frames too large', 'Non aligned frames', 'Short frames', 'CRC Errors', 'Overruns', 'Truncated frames', 'Trace to', 'Route hops', 'Response to end', 'Max ms', 'Loss to end', 'Max Loss', 'DNS Time', 'Target IP', 'Target RDNS', 'trace from', 'Up Percentile (%)', 'Up Bandwidth (Kbps)', 'Down Percentile (%)', 'Down Bandwidth (Kbps)', 'Download speed', 'Upload speed', 'D/load Cos', 'U/load Cos', 'Min RTT', 'Max RTT', 'Avg RTT', 'RTT Consistency', 'Max Delay', 'Avg Delay', 'Effective Speed', 'Route Speed', 'Forced Idle', 'Route Conc', 'Download test', 'Upload test', 'Errors', 'Errors', 'Average Latency', 'Minimum Latency', 'Maximum Latency', 'Ping Packet Loss', 'Average Latency', 'Failure', 'Minimum Latency', 'Test Port(s)', 'Maximum Latency', 'Opened', 'Failed', 'Refused', 'Timedout', 'TCP MTU', 'Pkts Norder', 'Bytes Norder', 'Pkts Xwindow', 'Bytes Xwindow', 'Pkts dup', 'Bytes dup', 'Pkts partdup', 'Bytes partdup', 'Pkts CRC errors', 'Pkts bad offset', 'Pkts too short', 'Wnd Probes Recvd', 'Zero wnd updates sent', 'Bytes lost', 'ReTx Timeouts', 'Fast ReTx', 'Pkts ReTx', 'Bytes ReTx', 'Wnd Closed', 'Pure Wnd Update', 'Acks for unsent', 'Dup acks', 'Wnd probes sent', 'Persist timeouts', 'Interface', 'XL Frames', 'NA Frames', 'Short Frames', 'CRC errors', 'Overruns', 'Cut Frames', 'Download Type', 'Upload Type', 'Network downtime (sec)', 'Network uptime (sec)', 'Network downtime (%)', 'HTTP 3xx (sec)', 'HTTP 4xx (sec)', 'HTTP 5xx (sec)', 'HTTP ?xx (sec)', 'Firmware Version', 'Runtime (sec)', 'FreeQ', 'Network downtime (sec)', 'Network uptime (sec)', 'Network downtime (%)', 'HTTP 3xx (sec)', 'HTTP 4xx (sec)', 'HTTP 5xx (sec)', 'HTTP ?xx (sec)', 'Firmware Version', 'Runtime (sec)', 'FreeQ', 'URL', 'Latency', 'Failure', 'Connect Latency', 'Find Latency', 'Read latency', 'Page Size', 'Kbps']
        # fieldnames_unused_voip = ['Download Speed (Kbps)', 'Upload Speed (Kbps)', 'Down Bandwidth (Kbps)', 'Up Bandwidth (Kbps)', 'Down Percentile (%)', 'Up Percentile (%)', 'CoS (%)', 'UCoS (%)', 'Min RTT', 'Max RTT', 'Avg RTT', 'Max route speed down(Kbps)', 'Up Route Speed (Kbps)', 'Max Delay (ms)', 'Up Delay (ms)', 'Effective speed (Kbps)', 'Up Effective speed (kbps)', 'Max TCP connections', 'Up Max TCP connections', 'TCP forced idle (%)', 'Up TCP forced idle (%)']
        # fieldnames_unused_speed = ['Upstream jitter', 'Downstream jitter', 'Upstream Maximum jitter', 'Downstream Maximum jitter', 'Upstream packet loss', 'Downstream packet loss', 'Upstream packet order', 'Downstream packet order', 'Packet discards', 'MOS', 'DMOS', 'Lines simulated', 'REGISTER ms', 'INVITE ms', 'BYE ms', 'RTTMin', 'RTTAvg', 'RTTMax', 'RTT Consistency', 'Upstream Loss distribution', 'Downstream Loss distribution', 'SIP ALG']
        
        fieldnames_for_voip = ['Date / Time','IP Address','Host Name','Test To','Test Spec','Session ID','Account Id','Country','Connection Type','Via Proxy','ISP','Record ID','Upstream jitter', 'Downstream jitter', 'Upstream Maximum jitter', 'Downstream Maximum jitter', 'Upstream packet loss', 'Downstream packet loss', 'Upstream packet order', 'Downstream packet order', 'Packet discards', 'MOS', 'DMOS', 'Lines simulated', 'REGISTER ms', 'INVITE ms', 'BYE ms', 'RTTMin', 'RTTAvg', 'RTTMax', 'RTT Consistency', 'Upstream Loss distribution', 'Downstream Loss distribution', 'SIP ALG']
        fieldnames_for_speed = ['Date / Time','IP Address','Host Name','Test To','Test Spec','Session ID','Account Id','Country','Connection Type','Via Proxy','ISP','Record ID','Download Speed (Kbps)', 'Upload Speed (Kbps)', 'Down Bandwidth (Kbps)', 'Up Bandwidth (Kbps)', 'Down Percentile (%)', 'Up Percentile (%)', 'CoS (%)', 'UCoS (%)', 'Min RTT', 'Max RTT', 'Avg RTT', 'Max route speed down(Kbps)', 'Up Route Speed (Kbps)', 'Max Delay (ms)', 'Up Delay (ms)', 'Effective speed (Kbps)', 'Up Effective speed (kbps)', 'Max TCP connections', 'Up Max TCP connections', 'TCP forced idle (%)', 'Up TCP forced idle (%)']

        # for campo in reader.fieldnames:
        #     if campo not in fieldnames_unused:
        #         if campo not in fieldnames_unused_voip:
        #             fieldnames_for_voip.append(campo)
        #         if campo not in fieldnames_unused_speed:
        #             fieldnames_for_speed.append(campo)

        writer_voip = csv.DictWriter(voip, delimiter=',', fieldnames=fieldnames_for_voip)
        writer_speed = csv.DictWriter(speed, delimiter=',', fieldnames=fieldnames_for_speed)

        writer_voip.writeheader()
        writer_speed.writeheader()
        cantidad_tests = 0
        for linea in reader:
            cantidad_tests+=1
            date_time,ip_address,hostname,testo,testspec,sessionid,accountid,country,connection_type,via_proxy,isp,record_id,up_jitter,down_jitter,up_max_jitter,down_max_jitter,up_loss,down_loss,up_pack_order,down_pack_order,pack_dis,up_mos,down_mos,lines_sim,register_ms,invite_ms,bye_ms,rtt_min,rtt_avg,rtt_max,rtt_cons,up_loss_dis,down_loss_dis,sip_alg,down_speed,up_speed,down_band,up_band,down_perc,up_perc,cos,ucos,min_rtt,max_rtt,avg_rtt,max_route_speed,up_route_speed,max_delay,up_delay,down_eff_speed,up_eff_speed,down_max_tcp,up_max_tcp,down_tcp_forced,up_tcp_forced= linea['Date / Time'],linea['IP Address'],linea['Host Name'],linea['Test To'],linea['Test Spec'],linea['Session ID'],linea['Account Id'],linea['Country'],linea['Connection Type'],linea['Via Proxy'],linea['ISP'],linea['Record ID'],linea['Upstream jitter'],linea[ 'Downstream jitter'],linea['Upstream Maximum jitter'],linea['Downstream Maximum jitter'],linea['Upstream packet loss'],linea['Downstream packet loss'],linea['Upstream packet order'],linea['Downstream packet order'],linea['Packet discards'],linea['MOS'],linea['DMOS'],linea['Lines simulated'],linea['REGISTER ms'],linea['INVITE ms'],linea['BYE ms'],linea['RTTMin'],linea['RTTAvg'],linea['RTTMax'],linea['RTT Consistency'],linea['Upstream Loss distribution'],linea['Downstream Loss distribution'],linea['SIP ALG'],linea['Download Speed (Kbps)'],linea['Upload Speed (Kbps)'],linea['Down Bandwidth (Kbps)'],linea['Up Bandwidth (Kbps)'],linea['Down Percentile (%)'],linea['Up Percentile (%)'],linea['CoS (%)'],linea['UCoS (%)'],linea['Min RTT'],linea['Max RTT'],linea['Avg RTT'],linea['Max route speed down(Kbps)'],linea['Up Route Speed (Kbps)'],linea['Max Delay (ms)'],linea['Up Delay (ms)'],linea['Effective speed (Kbps)'],linea['Up Effective speed (kbps)'],linea['Max TCP connections'],linea['Up Max TCP connections'],linea['TCP forced idle (%)'],linea['Up TCP forced idle (%)']
            if testspec == 'AV_VoIP_Test':
                writer_voip.writerow({fieldnames_for_voip[0]:date_time, fieldnames_for_voip[1]:ip_address, fieldnames_for_voip[2]:hostname,fieldnames_for_voip[3]:testo,fieldnames_for_voip[4]:testspec,fieldnames_for_voip[5]:sessionid,fieldnames_for_voip[6]:accountid,fieldnames_for_voip[7]:country,fieldnames_for_voip[8]:connection_type,fieldnames_for_voip[9]:via_proxy,fieldnames_for_voip[10]:isp,fieldnames_for_voip[11]:record_id, \
                fieldnames_for_voip[12]:up_jitter, fieldnames_for_voip[13]:down_jitter,fieldnames_for_voip[14]:up_max_jitter,fieldnames_for_voip[15]:down_max_jitter,fieldnames_for_voip[16]:up_loss,fieldnames_for_voip[17]:down_loss, \
                fieldnames_for_voip[18]: up_pack_order, fieldnames_for_voip[19]:down_pack_order, fieldnames_for_voip[20]:pack_dis,fieldnames_for_voip[21]:up_mos,fieldnames_for_voip[22]:down_mos,fieldnames_for_voip[23]:lines_sim,fieldnames_for_voip[24]:register_ms,fieldnames_for_voip[25]:invite_ms, \
                fieldnames_for_voip[26]:bye_ms, fieldnames_for_voip[27]:rtt_min,fieldnames_for_voip[28]:rtt_avg,fieldnames_for_voip[29]:rtt_max,fieldnames_for_voip[30]:rtt_cons,fieldnames_for_voip[31]:up_loss_dis,fieldnames_for_voip[32]:down_loss_dis, \
                fieldnames_for_voip[33]:sip_alg})
            if testspec == 'AV_Speed_Test':
                writer_speed.writerow({fieldnames_for_speed[0]:date_time, fieldnames_for_speed[1]:ip_address, fieldnames_for_speed[2]:hostname,fieldnames_for_speed[3]:testo,fieldnames_for_speed[4]:testspec,fieldnames_for_speed[5]:sessionid,fieldnames_for_speed[6]:accountid,fieldnames_for_speed[7]:country,fieldnames_for_speed[8]:connection_type,fieldnames_for_speed[9]:via_proxy,fieldnames_for_speed[10]:isp,fieldnames_for_speed[11]:record_id, \
                fieldnames_for_speed[12]:down_speed,fieldnames_for_speed[13]:up_speed,fieldnames_for_speed[14]:down_band,fieldnames_for_speed[15]:up_band,fieldnames_for_speed[16]:down_perc,fieldnames_for_speed[17]:up_perc,fieldnames_for_speed[18]:cos,fieldnames_for_speed[19]:ucos,fieldnames_for_speed[20]:min_rtt,fieldnames_for_speed[21]:max_rtt, \
                fieldnames_for_speed[22]:avg_rtt,fieldnames_for_speed[23]:max_route_speed,fieldnames_for_speed[24]:up_route_speed,fieldnames_for_speed[25]:max_delay,fieldnames_for_speed[26]:up_delay,fieldnames_for_speed[27]:down_eff_speed,fieldnames_for_speed[28]:up_eff_speed,fieldnames_for_speed[29]:down_max_tcp,fieldnames_for_speed[30]:up_max_tcp,\
                fieldnames_for_speed[31]:down_tcp_forced,fieldnames_for_speed[32]:up_tcp_forced })
            
        archivo_info.write(f'=== INFO ===\n Total tests: {cantidad_tests}\n Location: {country}\n ISP: {isp}\n Test To: {testo}\n Probe Name: {sessionid.split("/")[2]}')


def convertir_a_csv(archivo_base,archivo_convertido):
    with open (archivo_base, 'r',encoding='utf-8') as archivo_base, open(archivo_convertido, 'w', newline='', encoding='utf-8') as archivo_convertido:
        reader = csv.DictReader(archivo_base,delimiter='\t')
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(archivo_convertido, delimiter=',',fieldnames=fieldnames)
        writer.writeheader()
        for linea in reader: 
            writer.writerow(linea)

def voip_data_cleaner(archivo_origen, archivo_destino):
    with open (archivo_origen, 'r',encoding='utf-8') as ao, open (archivo_destino, 'w',encoding='utf-8',newline='') as ad:
        reader = csv.DictReader(ao, delimiter=",")
        fieldnames = reader.fieldnames + ['UpJitterAboveThreshold', 'DoJitterAboveThreshold','UpVoAboveThreshold', 'DoVoAboveThreshold', 'DMOS-TH', 'MOS-TH']

        writer = csv.DictWriter(ad, delimiter=',', fieldnames=fieldnames)
        writer.writeheader()

        for linea_origen in reader:
            _,_,_,_,_,_,_,_,_,_,_,_,up_jitter,down_jitter,_,_,up_loss,down_loss,_,_,_,up_mos,down_mos,_,_,_,_,_,_,_,_,_,_,_ = linea_origen.values()
            
            linea_origen['UpJitterAboveThreshold'] = 1 if values_above_threshold(up_jitter, 'up_jitter', 30) else 0
            linea_origen['DoJitterAboveThreshold'] = 1 if values_above_threshold(down_jitter, 'down_jitter', 30) else 0
            linea_origen['UpVoAboveThreshold'] = 1 if values_above_threshold(up_loss, 'up_loss', 1) else 0
            linea_origen['DoVoAboveThreshold'] = 1 if values_above_threshold(down_loss, 'down_loss', 1) else 0
            linea_origen['MOS-TH'] = 1 if values_above_threshold(up_mos, 'up_mos', 3) else 0
            linea_origen['DMOS-TH'] = 1 if values_above_threshold(down_mos, 'down_mos', 3) else 0

            writer.writerow(linea_origen)

def values_above_threshold(valor, medida, threshold):
    medidas_jitter_loss = ['up_jitter', 'down_jitter', 'up_loss','down_loss']
    medidas_mos = ['up_mos','down_mos']
    try:
        if medida in medidas_jitter_loss:
            if float(valor) > threshold:
                return True
        elif medida in medidas_mos:
            if float(valor) < threshold:
                return True
        else:
            raise MedidaInvalidaError
    except ValueError:
        print("No se pudo convertir valor porque es - (nulo)")

def speed_data_cleaner(archivo_origen, archivo_destino):
    with open(archivo_origen, 'r', encoding='utf-8') as archivo_origen, open(archivo_destino, 'w', encoding='utf-8', newline='') as archivo_destino:
        reader = csv.DictReader(archivo_origen, delimiter=',')
        fieldnames = reader.fieldnames + ['Effective speed (Mbps)','Up Effective speed (Mbps)']
        writer = csv.DictWriter(archivo_destino, delimiter=',', fieldnames=fieldnames)

        writer.writeheader()

        for linea in reader:
            linea['Effective speed (Mbps)'] = float(linea['Effective speed (Kbps)']) / 1000
            linea['Up Effective speed (Mbps)'] = float(linea['Up Effective speed (kbps)']) / 1000

            writer.writerow(linea)
def define_customer_name():
    customer_name = input('Please type the Customer Name...\t ')
    return customer_name
def define_path_to_tsv():
    path_to_tsv = input('Please type the path to the .tsv file...\t')
    return f'{current}/{path_to_tsv}'


def processing(path_to_tsv, customer_name):
    print('-=-=-=-=-[PROCESSING]-=-=-=-=-')
    os.makedirs(f'{current}/{customer_name}')
    convertir_a_csv(path_to_tsv,f'{current}/{customer_name}/runonflytemplate.csv')
    general_data_cleaner(f'{current}/{customer_name}/runonflytemplate.csv',f'{current}/{customer_name}/{customer_name}_VoIPTest.csv',f'{current}/{customer_name}/{customer_name}_SpeedTest.csv', f'{current}/{customer_name}/{customer_name}_TestINFO.txt')
    voip_data_cleaner(f'{current}/{customer_name}/{customer_name}_VoIPTest.csv',f'{current}/{customer_name}/{customer_name}_VoIPTest_FULL.csv')
    speed_data_cleaner(f'{current}/{customer_name}/{customer_name}_SpeedTest.csv',f'{current}/{customer_name}/{customer_name}_SpeedTest_FULL.csv')
    print('-=-=-=-=-[END PROCESSING]-=-=-=-=-')

if __name__ == '__main__':
    switcher = {"1": lambda: processing(path_to_tsv=define_path_to_tsv(), customer_name=define_customer_name())}
    
    # convertir_a_csv('C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/runonflytemplate.tsv','C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/runonflytemplate.csv')
    # general_data_cleaner('C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/runonflytemplate.csv', 'C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/voip.csv', 'C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/speed.csv','C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/info.txt' )
    # voip_data_cleaner('C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/voip.csv', 'C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/voip_full.csv')
    # speed_data_cleaner('C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/speed.csv', 'C:/Users/Naranja/Documents/facu/2022 2H/EDD/Datadata_cleaner/speed_full.csv')

    while True:

            print("\n\t.: MCS Data Cleaner :.\n")
            print("\t1: Start processing")

            op=input("\nChoose an option: ")
            resultado_menu = switcher[op]()
            
            exit=input("Continue using menu [y/n] ")
            if exit[0].lower() != "y":
                break

import cx_Oracle
import xlrd
import pandas as pd

def query(script):
    data = xlrd.open_workbook('') #Location of Credentials
    data_sheet = data.sheet_by_index(0)
    UID = data_sheet.cell_value(1, 0)
    PWD = data_sheet.cell_value(1, 1)
    conn = cx_Oracle.connect(UID, PWD, "DWRAC_UMB_UUMG")
    df = pd.read_sql_query(script, conn)
    print(df.to_string())

def provider():
    userInput = input("Please enter Provider Name in this format [LastName, FirstName]:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT EPIC_PROV_ID, PROV_ID, PROV_NAME, PROV_TYPE, DEPARTMENT,
                    UUHC_BEGIN_APPT_DATE "START_DATE", UUHC_END_APPT_DATE "END_DATE" 
                     FROM PROVIDER_DM.PROVIDER_MASTER_VW 
                     WHERE UPPER(PROV_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def provider2():
    userInput = input("Please enter Provider Name in this format [LastName, FirstName]:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT PROV_ID, PROV_NAME, PROV_TYPE
                     FROM CLARITY_REPORT.CLARITY_SER
                     WHERE UPPER(PROV_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def billArea():
    userInput = input("Please enter part of the Bill Area Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT BILL_AREA_ID, RECORD_NAME "BILL AREA NAME"
                     FROM CLARITY_REPORT.BILL_AREA
                     WHERE UPPER(RECORD_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def department():
    userInput = input("Please enter part of the Scheduling Department Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DEPARTMENT_ID, DEPARTMENT_NAME
                     FROM CLARITY_REPORT.CLARITY_DEP
                     WHERE UPPER(DEPARTMENT_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def payor():
    userInput = input("Please enter part of the Payor Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT PAYOR_ID, PAYOR_NAME
                     FROM CLARITY_REPORT.CLARITY_EPM
                     WHERE UPPER(PAYOR_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def pos():
    userInput = input("Please enter part of the POS Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT POS_ID, POS_NAME, POS_TYPE_C
                     FROM CLARITY_REPORT.CLARITY_POS
                     WHERE UPPER(POS_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def posgroup():
    userInput = input("Please enter part of the POS Group Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT POS_GROUP, NAME, TITLE, ABBR 
                     FROM CLARITY_REPORT.ZC_POS_GROUP
                     WHERE UPPER(NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def cptDesc():
    userInput = input("Please enter part of the CPT Name (PROC_NAME):  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT PROC_ID, PROC_CODE "CPT_CODE", PROC_NAME,  SHORT_NAME
                     FROM CLARITY_REPORT.CLARITY_EAP
                     WHERE UPPER(PROC_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def cptCode():
    userInput = input("Please enter the entire CPT Code:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT PROC_ID, PROC_CODE "CPT_CODE", PROC_NAME,  SHORT_NAME
                     FROM CLARITY_REPORT.CLARITY_EAP
                     WHERE UPPER(PROC_CODE) = \'''' + str(search_name) + '\'')
    query(script)

def sos():
    userInput = input("Please enter the SOS ID (22, 20822, 11 etc.):  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT POS_TYPE_C, NAME
                     FROM CLARITY_REPORT.ZC_POS_TYPE
                     WHERE POS_TYPE_C =''' + str(search_name) + '')
    query(script)

def group():
    userInput = input("Please enter part of the Billing Group Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT RPT_GRP_12_BIL_C, NAME, TITLE, ABBR 
                     FROM CLARITY_REPORT.ZC_RPT_GRP_12_BIL
                     WHERE UPPER(NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def altdiv():
    userInput = input("Please enter part of the Alternate Division Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT RPT_GRP_16_BIL_C, NAME, TITLE, ABBR 
                     FROM CLARITY_REPORT.ZC_RPT_GRP_16_BIL
                     WHERE UPPER(NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def billdiv():
    userInput = input("Please enter part of the Division Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT RPT_GRP_11_BIL_C, NAME, TITLE, ABBR 
                     FROM CLARITY_REPORT.ZC_RPT_GRP_11_BIL
                     WHERE UPPER(NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def plan():
    userInput = input("Please enter part of the Payor Benefit Plan Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT EPP.BENEFIT_PLAN_ID, EPP.BENEFIT_PLAN_NAME, EPP.PRODUCT_TYPE, EPM.PAYOR_NAME
                     FROM CLARITY_REPORT.CLARITY_EPP EPP
                     LEFT JOIN CLARITY_REPORT.CLARITY_EPM EPM ON EPM.PAYOR_ID = EPP.PAYOR_ID
                     WHERE UPPER(EPP.BENEFIT_PLAN_NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def finclass():
    userInput = input("Please enter part of the Financial Class Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT FINANCIAL_CLASS, NAME, TITLE, ABBR
                     FROM CLARITY_REPORT.ZC_FINANCIAL_CLASS
                     WHERE UPPER(NAME) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def dwid_detail_type():
    userInput = input("Please enter part of the Detail Type Name (i.e. 'Charge','Payment' etc.):  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DWID, DOMAIN, CODE, D_PB_TX_DETAIL_TYPE_DESC, STATUS, SOURCE, LOAD_DATE 
                     FROM VOCAB.D_PB_TX_DETAIL_TYPE
                     WHERE UPPER(D_PB_TX_DETAIL_TYPE_DESC) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def payorDW():
    userInput = input("Please enter part of the Payor Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DWID, DOMAIN, CODE, D_PAYOR_DESC, STATUS, SOURCE, LOAD_DATE 
                     FROM VOCAB.D_PAYOR
                     WHERE UPPER(D_PAYOR_DESC) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def planDW():
    userInput = input("Please enter part of the Plan Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DWID, DOMAIN, CODE, D_PLAN_DESC, STATUS, SOURCE, LOAD_DATE 
                     FROM VOCAB.D_PLAN
                     WHERE UPPER(D_PLAN_DESC) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def finclassDW():
    userInput = input("Please enter part of the Financial Class Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DWID, DOMAIN, CODE, D_FINAN_CLASS_DESC, STATUS, SOURCE, LOAD_DATE 
                     FROM VOCAB.D_FINAN_CLASS
                     WHERE UPPER(D_FINAN_CLASS_DESC) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def groupDW():
    userInput = input("Please enter part of the Billing Group Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DWID, DOMAIN, CODE, D_BILL_AREA_GROUP_DESC, STATUS, SOURCE, LOAD_DATE 
                     FROM VOCAB.D_BILL_AREA_GROUP
                     WHERE UPPER(D_BILL_AREA_GROUP_DESC) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def billdivDW():
    userInput = input("Please enter part of the Division Name:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DWID, DOMAIN, CODE, D_BILL_AREA_DIVISION_DESC, STATUS, SOURCE, LOAD_DATE 
                     FROM VOCAB.D_BILL_AREA_DIVISION
                     WHERE UPPER(D_BILL_AREA_DIVISION_DESC) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def cptDWdesc():
    userInput = input("Please enter part of the CPT name (PROC_NAME):  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT PROC_CODE_DWID,	PROC_CODE,	PROC_CODE_DESC,	UPDATE_DTM
                     FROM VOCAB.PROC_CODE_MASTER
                     WHERE UPPER(PROC_CODE_DESC) LIKE \'%''' + str(search_name) + '%\'')
    query(script)

def cptDWcode():
    userInput = input("Please enter the entire CPT Code:  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT PROC_CODE_DWID,	PROC_CODE,	PROC_CODE_DESC,	UPDATE_DTM
                     FROM VOCAB.PROC_CODE_MASTER
                     WHERE UPPER(PROC_CODE) = \'''' + str(search_name) + '\'')
    query(script)

def sosDW():
    userInput = input("Please enter the SOS ID (22, 20822, 11 etc.):  ")
    print('-----------------------------------------------------------------------------')
    search_name = userInput.upper()
    script = str(''' SELECT DWID, DOMAIN, CODE, D_POS_TYPE_DESC, STATUS, SOURCE, LOAD_DATE 
                     FROM VOCAB.D_POS_TYPE
                     WHERE CODE =''' + str(search_name) + '')
    query(script)

print('''What are you searching for? 

[1]  Provider - Provider_DM      [13] Billing Division
[2]  Provider - Clarity_SER      [14] Payor Benefit Plan
[3]  Bill Area                   [15] Financial Class
[4]  Department                  [16] DWID Detail Type
[5]  Payor                       [17] DWID Payor
[6]  POS                         [18] DWID Plan
[7]  POS Group                   [19] DWID Financial Class
[8]  CPT by Description          [20] DWID Billing Group
[9]  CPT by Code                 [21] DWID Billing Division
[10] SOS                         [22] DWID CPT by Description
[11] Billing Group               [23] DWID CPT by Code
[12] Alternate Division          [24] DWID SOS

Please enter the corresponding number.''')

choice = input('>>> ')
print('')

while choice.upper() != 'QUIT':
    try:
        if int(choice) == 1:
            provider()
        elif int(choice) == 2:
            provider2()
        elif int(choice) == 3:
            billArea()
        elif int(choice) == 4:
            department()
        elif int(choice) == 5:
            payor()
        elif int(choice) == 6:
            pos()
        elif int(choice) == 7:
            posgroup()
        elif int(choice) == 8:
            cptDesc()
        elif int(choice) == 9:
            cptCode()
        elif int(choice) == 10:
            sos()
        elif int(choice) == 11:
            group()
        elif int(choice) == 12:
            altdiv()
        elif int(choice) == 13:
            billdiv()
        elif int(choice) == 14:
            plan()
        elif int(choice) == 15:
            finclass()
        elif int(choice) == 16:
            dwid_detail_type()
        elif int(choice) == 17:
            payorDW()
        elif int(choice) == 18:
            planDW()
        elif int(choice) == 19:
            finclassDW()
        elif int(choice) == 20:
            groupDW()
        elif int(choice) == 21:
            billdivDW()
        elif int(choice) == 22:
            cptDWdesc()
        elif int(choice) == 23:
            cptDWcode()
        elif int(choice) == 24:
            sosDW()
    except Exception as e:
        print("Unexpected Error:", str(e))
    print('-----------------------------------------------------------------------------')
    print('''
[1]  Provider - Provider_DM      [13] Billing Division
[2]  Provider - Clarity_SER      [14] Payor Benefit Plan
[3]  Bill Area                   [15] Financial Class
[4]  Department                  [16] DWID Detail Type
[5]  Payor                       [17] DWID Payor
[6]  POS                         [18] DWID Plan
[7]  POS Group                   [19] DWID Financial Class
[8]  CPT by Description          [20] DWID Billing Group
[9]  CPT by Code                 [21] DWID Billing Division
[10] SOS                         [22] DWID CPT by Description
[11] Billing Group               [23] DWID CPT by Code
[12] Alternate Division          [24] DWID SOS

Please choose another category to search or type \'quit\' to exit.''')
    choice = input('>>> ')
    print('')

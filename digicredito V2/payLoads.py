""" EN ESTE ARCHIVO SE VAN A MANEJAR SOLO LOS PAYLOADS, SE TRAERA LA DATA PROCEDURAL DESDE CASESLISTAS
Y SE INSERTARA EN LOS PAYLOADS"""
import random
import casesListas as cl

simuladorPricing = {
        "idPagaduria": 0,
        "idAsesor": 2895,
        "idOficina": 0,
        "idLineaCredito": 1,
        "subCanal": "WEB",
        "actividadCliente": "",
        "tasa": 0,
        "plazo": 0,
        "monto": 0,
        "diasInteresesIniciales": 120,
        "ingresos": 0,
        "descuentosLey": 0,
        "descuentosNomina": 0,
        "medioContacto": "EMPRESA_TRABAJO_CLIENTE",
        "carteras": [],
        "cliente": {
            "primerNombre": "",
            "segundoNombre": "",
            "primerApellido": "",
            "segundoApellido": "",
            "tipoIdentificacion": "CC",
            "identificacion": 0,
            "fechaNacimiento": "0000-00-00",
            "celular": "",
            "email": "",
            "idCiudad": "",
            "departamento": ""
        },
        "departamento": "",
        "ciudad": {
            "id": "",
            "nombre": "",
            "codigo": "null",
            "departamento": "null"
        },
        "validarIdentidad": True,
        "genero": "",
        "totalActivos": "",
        "estrato": "",
        "productPricing": {},
        "nivelEducativo": "",
        "tipoContrato": ""
    }

simuladorVersion = {
    "idPagaduria": 0,
    "idAsesor": 2895,
    "idOficina": 0,
    "idLineaCredito": 1,
    "subCanal": "WEB",
    "actividadCliente": "PENSIONADO",
    "tasa": 0,
    "plazo": 0,
    "monto": 0,
    "diasInteresesIniciales": 120,
    "ingresos": 0,
    "descuentosLey": 0,
    "descuentosNomina": 0,
    "medioContacto": "ASESOR",
    "carteras": [],
    "cliente": {
        "primerNombre": "",
        "segundoNombre": "",
        "primerApellido": "",
        "segundoApellido": "",
        "tipoIdentificacion": "CC",
        "identificacion": 0,
        "fechaNacimiento": "",
        "celular": "",
        "email": "",
        "idCiudad": "",
        "departamento": ""
    },
    "departamento": "",
    "ciudad": {
        "id": "",
        "nombre": "",
        "codigo": "null",
        "departamento": "null"
    },
    "validarIdentidad": True,
    "genero": ""
}

compra = {
            "id": "null",
            "idCredito": "null",
            "idCompetidor": "null",
            "monto": "",
            "valorCuota": "null",
            "fechaVencimiento": "",
            "noObligacion": "null",
            "tipoCartera": "null",
            "estado": "null",
            "gmf": "null"
        }

def dataSimulador(data):
    if data['isPricing'] == True:
        simuladorPricing['cliente']['primerNombre'] = data['nombre1']
        simuladorPricing['cliente']['segundoNombre'] = data['nombre2']
        simuladorPricing['cliente']['primerApellido'] = data['apellido1']
        simuladorPricing['cliente']['segundoApellido'] = data['apellido2']
        simuladorPricing['cliente']['identificacion'] = data['identificacion']
        simuladorPricing['cliente']['fechaNacimiento'] = data['fechaNacimiento']
        simuladorPricing['cliente']['celular'] = data['celular']
        simuladorPricing['cliente']['email'] = data['email']
        simuladorPricing['cliente']['idCiudad'] = data['ciudad']
        simuladorPricing['cliente']['departamento'] = data['departamento']
        simuladorPricing['idPagaduria'] = data['idPagaduria']
        simuladorPricing['idOficina'] = data['idOficina']
        simuladorPricing['plazo'] = data['plazo']
        simuladorPricing['monto'] = data['montoSolicitado']
        simuladorPricing['ingresos'] = data['totalIngresos']
        simuladorPricing['descuentosLey'] = data['descuentosLey']
        simuladorPricing['descuentosNomina'] = data['descuentosNomina']
        simuladorPricing['departamento'] = data['departamento']
        simuladorPricing['ciudad']['id'] = data['ciudad']
        simuladorPricing['ciudad']['nombre'] = data['nCiudad']
        simuladorPricing['genero'] = data['genero']
        simuladorPricing['totalActivos'] = str(data['totalActivos'])
        simuladorPricing['estrato'] = data['nomEstrato']
        simuladorPricing['nivelEducativo'] = data['nivelEducacion']
        simuladorPricing['tipoContrato'] = data['tipoContrato']
        simuladorPricing['actividadCliente'] = data['actividadEconomica']
        simuladorPricing['tasa'] = float(data['tasa'])
        simuladorPricing['productPricing']['rate'] = float(data['tasa'])
        simuladorPricing['productPricing']['suretyBond'] = data['dataPricing']['suretyBond']
        simuladorPricing['productPricing']['creditStudy'] = data['dataPricing']['creditStudy']
        simuladorPricing['productPricing']['productGroupId'] = data['dataPricing']['productGroupId']
        simuladorPricing['productPricing']['deterioration'] = data['dataPricing']['deterioration']
        simuladorPricing['productPricing']['rates'] = data['dataPricing']['rates']
        simuladorPricing['productPricing']['groupNumber'] = data['dataPricing']['groupNumber']
        if data['conCompra'] == True:
            simuladorPricing['idLineaCredito'] = 4
            cartera = compra
            cartera['monto'] = str(data['compraCartera'])
            simuladorPricing['carteras'].append(cartera)
        if data['tieneRetanqueo'] == True:
            idCreditoPadre = []
            print(data)
            i = data['creditoPadre']
            idCreditoPadre.append(i)
            simuladorPricing['idLineaCredito'] = 3
            simuladorPricing['idCreditoPadre'] = idCreditoPadre
        if data['tieneRetanqueo'] and data['conCompra'] == True:
            simuladorPricing['idLineaCredito'] = 5
        return simuladorPricing
    else:
        simuladorVersion['cliente']['primerNombre'] = data['nombre1']
        simuladorVersion['cliente']['segundoNombre'] = data['nombre2']
        simuladorVersion['cliente']['primerApellido'] = data['apellido1']
        simuladorVersion['cliente']['segundoApellido'] = data['apellido2']
        simuladorVersion['cliente']['identificacion'] = data['identificacion']
        simuladorVersion['cliente']['fechaNacimiento'] = data['fechaNacimiento']
        simuladorVersion['cliente']['celular'] = data['celular']
        simuladorVersion['cliente']['email'] = data['email']
        simuladorVersion['cliente']['idCiudad'] = data['ciudad']
        simuladorVersion['cliente']['departamento'] = data['departamento']
        simuladorVersion['idPagaduria'] = data['idPagaduria']
        simuladorVersion['idOficina'] = data['idOficina']
        simuladorVersion['plazo'] = data['plazo']
        simuladorVersion['monto'] = data['montoSolicitado']
        simuladorVersion['ingresos'] = data['totalIngresos']
        simuladorVersion['descuentosLey'] = data['descuentosLey']
        simuladorVersion['descuentosNomina'] = data['descuentosNomina']
        simuladorVersion['departamento'] = data['departamento']
        simuladorVersion['ciudad']['id'] = data['ciudad']
        simuladorVersion['ciudad']['nombre'] = data['nCiudad']
        simuladorVersion['genero'] = data['genero']
        simuladorVersion['tasa'] = data['tasa']
        simuladorVersion['actividadCliente'] = data['actividadEconomica']
        if data['conCompra'] == True:
            simuladorVersion['idLineaCredito'] = 4
            cartera = compra
            cartera['monto'] = str(data['compraCartera'])
            simuladorVersion['carteras'].append(cartera)
        if data['tieneRetanqueo'] == True:
            idCreditoPadre = []
            i = data['creditoPadre']
            idCreditoPadre.append(i)
            simuladorPricing['idLineaCredito'] = 3
            simuladorPricing['idCreditoPadre'] = idCreditoPadre
        if data['tieneRetanqueo'] and data['conCompra'] == True:
            simuladorPricing['idLineaCredito'] = 5
        return simuladorVersion

destinoCredito = {
    "cadena": "",
    "idDestino": "2",
    "destino": "Educación"
}

validarOtp = {
    "cadena": "",
    "otp": "",
    "canalContacto": {
        "otp": "",
        "correoElectronico": True,
        "mensajeTexto": True,
        "celularTelefonoFijo": True,
        "residencia": True,
        "otros": True
    }
}

completarCliente = {
    "idSimulacion": "",
    "idAsesorAutorizado": "2895",
    "idDepartamento": "",
    "idCiudad": "",
    "tipoIdentificacion": "CC",
    "identificacion": "",
    "primerNombre": "",
    "segundoNombre": "",
    "primerApellido": "",
    "segundoApellido": "",
    "fechaNacimiento": "",
    "fechaExpedicionDocumento": "",
    "ciudadExpedicionIdentificacion": "",
    "genero": "",
    "celular": "",
    "email": "",
    "subCanal": "WEB",
    "soloActualizar": "true"
}

def compleCliente(data):
    completarCliente['idDepartamento'] = data['departamento']
    completarCliente['idCiudad'] = data['ciudad']
    completarCliente['identificacion'] = data['identificacion']
    completarCliente['primerNombre'] = data['nombre1']
    completarCliente['segundoNombre'] = data['nombre2']
    completarCliente['primerApellido'] = data['apellido1']
    completarCliente['segundoApellido'] = data['apellido2']
    completarCliente['fechaNacimiento'] = data['fechaNacimiento']
    completarCliente['fechaExpedicionDocumento'] = data['fechaExpedicion']
    completarCliente['ciudadExpedicionIdentificacion'] = data['ciudad']
    completarCliente['genero'] = data['genero']
    completarCliente['celular'] = data['celular']
    completarCliente['email'] = data['email']
    return completarCliente

globalDebt = {
    "save": "false",
    "idCredito": "",
    "idEstrato": "",
    "idTipoVivienda": "",
    "idClaseVivienda": "",
    "idParentesco": "",
    "idNivelEducativo": "",
    "descuentosPrestacionales": "",
    "descuentosNomina": "",
    "cuotasHipotecariasCentrales": "",
    "idDocumento": "Desprendible de Nomina",
    "subCanal": "WEB"
}

def endeudamientoGlobal(data):
    globalDebt['idEstrato'] = data['idStrato']
    globalDebt['idTipoVivienda'] = data['tipoVivienda']
    globalDebt['idClaseVivienda'] = str(data['tipoRecidencia'])
    globalDebt['idParentesco'] = str(data['posicionHogar'])
    globalDebt['idNivelEducativo'] = data['idNivelEducacion']
    globalDebt['descuentosPrestacionales'] = str(data['descuentosLey'])
    globalDebt['descuentosNomina'] = str(data['descuentosNomina'])
    globalDebt['cuotasHipotecariasCentrales'] = str(data['descuentosLey'])
    return globalDebt

globalDebt2 = {
    "save": "true",
    "idCredito": "",
    "idEstrato": "",
    "idTipoVivienda": "",
    "idClaseVivienda": "",
    "idParentesco": "",
    "idNivelEducativo": "",
    "descuentosPrestacionales": "",
    "descuentosNomina": "",
    "cuotasHipotecariasCentrales": "1",
    "ingresosAdicionales": "0",
    "idDocumento": "Desprendible de Nomina"
}

def endeudamientoGlobal2(data):
    globalDebt2['idEstrato'] = data['idStrato']
    globalDebt2['idTipoVivienda'] = data['tipoVivienda']
    globalDebt2['idClaseVivienda'] = data['tipoRecidencia']
    globalDebt2['idParentesco'] = data['posicionHogar']
    globalDebt2['idNivelEducativo'] = data['idNivelEducacion']
    globalDebt2['descuentosPrestacionales'] = data['descuentosLey']
    globalDebt2['descuentosNomina'] = data['descuentosNomina']
    globalDebt2['cuotasHipotecariasCentrales'] = data['descuentosLey']
    return globalDebt2

medioDesembolso = {
    "idCredito": 0,
    "numeroCuenta": "1234567",
    "idTipoCuenta": "AHORROS",
    "idDepartamento": "",
    "idCiudad": "",
    "idModalidadDesembolso": "ACH",
    "idTipoCliente": "Producto Reportado",
    "idEntidadFinanciera": 0
}

medioDeDesembolso2 = {
    "idCredito": 0,
    "idModalidadDesembolso": "PAGO_MASIVO",
    "idTipoCliente": "Producto Reportado"
}

def medioDeDesembolso(data):
    medioDesembolso['idDepartamento'] = data['departamento']
    medioDesembolso['idCiudad'] = data['ciudad']
    medioDesembolso['idEntidadFinanciera'] = data['banco']['id']
    return medioDesembolso

aditionalData = {
    "idCredito": 0,
    "cliente": {
        "direcciones": [
            {
                "tipo": "7",
                "direccion": "AC 1 # 1 - 1",
                "barrio": "Barrio",
                "departamento": "",
                "ciudad": ""
            },
            {
                "tipo": "9",
                "direccion": "AC 1 # 1 - 1",
                "barrio": "Barrio",
                "departamento": "",
                "ciudad": ""
            }
        ]
    },
    "credito": {
        "mesesResidenciaActual": "0",
        "numeroHijos": "0",
        "personasACargo": "0",
        "tieneVehiculo": "false"
    }
}

def addData (data):
    aditionalData['cliente']['direcciones'][0]['departamento'] = data['departamento']
    aditionalData['cliente']['direcciones'][1]['departamento'] = data['departamento']
    aditionalData['cliente']['direcciones'][0]['ciudad'] = data['ciudad']
    aditionalData['cliente']['direcciones'][1]['ciudad'] = data['ciudad']
    return aditionalData

basiData = {
    "idCredito": 0,
    "cliente": {
        "paisNacimiento": "Colombia",
        "lugarNacimiento": "Albania (Santander)",
        "nacionalidad": "Colombiana",
        "genero": "",
        "grupoEtnico": 6
    },
    "credito": {
        "estadoCivil": "VIUDO",
        "profesion": "marineroQA"
    }
}

def basData(data):
    basiData['cliente']['genero'] = data['genero']
    return basiData

wrksData = {
    "idCredito": "",
    "fechaIngreso": "",
    "actividad": "",
    "nitAfiliacion": "",
    "tipoPension": "",
    "cargo": "DummyQA",
    "idDocumento": "Carta Laboral",
    "telefonoTrabajo": "6016612",
    "extensionTelefonoTrabajo": ""
}

def wrkData(data):
    wrksData['fechaIngreso'] = data['fechaIngreso']
    wrksData['actividad'] = data['actividadEconomica']
    # if data['actividadEconomica'] == 'PENSIONADO'or data['actividadEconomica'] == 'JUBILADO':
    wrksData['tipoPension'] = data['tipoContrato']
    if data['pagaduria'] == 'P.A COLPENSIONES':
        wrksData['nitAfiliacion'] = '123456789012'
    return wrksData


simulator2pricing = {
    "idPagaduria": 0,
    "idLineaCredito": 0,
    "idOficina": 0,
    "actividadCliente": "",
    "tasa": 0,
    "plazo": 0,
    "monto": 0,
    "diasInteresesIniciales": 120,
    "ingresos": 0,
    "cliente": {
        "identificacion": "",
        "fechaNacimiento": ""
    },
    "descuentosLey": 0,
    "descuentosNomina": 0,
    "carteras": [],
    "departamento": "",
    "genero": "",
    "nivelEducativo": "",
    "tipoContrato": "",
    "productPricing": {
        "rate": 0,
        "suretyBond": 0,
        "creditStudy": 0,
        "productGroupId": 0,
        "deterioration": 0,
        "rates": [],
        "groupNumber": 0
    },
    "totalActivos": 0,
    "estrato": ""
}

simulator2 = {
    "idPagaduria": 0,
    "idLineaCredito": 0,
    "idOficina": 0,
    "actividadCliente": "",
    "tasa": 0,
    "plazo": 0,
    "monto": 0,
    "diasInteresesIniciales": 120,
    "ingresos": 0,
    "cliente": {
        "identificacion": "",
        "fechaNacimiento": ""
    },
    "descuentosLey": 0,
    "descuentosNomina": 0,
    "carteras": [],
    "departamento": "",
    "genero": "",
    "nivelEducativo": "",
    "totalActivos": 0
}

compra2 ={
    "id": "null",
    "idCredito": "null",
    "idCompetidor": 1895,
    "monto": "",
    "valorCuota": 200000,
    "fechaVencimiento": "2024-12-12",
    "noObligacion": 1234567,
    "tipoCartera": "null",
    "estado": "null",
    "gmf": "null"
}
    
def dataSim2(data):
    if data['isPricing'] == True:
        simulator2pricing['idPagaduria'] = data['idPagaduria']
        simulator2pricing['idOficina'] = data['idOficina']
        simulator2pricing['actividadCliente'] = data['actividadEconomica']
        taza = data['dataPricing']['rates'][random.randrange(len(data['dataPricing']['rates']))]
        simulator2pricing['tasa'] = taza
        simulator2pricing['plazo'] = data['plazo']
        simulator2pricing['monto'] = data['montoSolicitado']
        simulator2pricing['ingresos'] = data['totalIngresos']
        simulator2pricing['cliente']['identificacion'] = data['identificacion']
        simulator2pricing['cliente']['fechaNacimiento'] = data['fechaNacimiento']
        simulator2pricing['descuentosLey'] = data['descuentosLey']
        simulator2pricing['descuentosNomina'] = data['descuentosNomina']
        simulator2pricing['departamento'] = data['departamento']
        simulator2pricing['genero'] = data['genero']
        simulator2pricing['nivelEducativo'] = data['nivelEducacion']
        simulator2pricing['tipoContrato'] = data['tipoContrato']
        simulator2pricing['productPricing']['rate'] = taza
        simulator2pricing['productPricing']['suretyBond'] = data['dataPricing']['suretyBond']
        simulator2pricing['productPricing']['creditStudy'] = data['dataPricing']['creditStudy']
        simulator2pricing['productPricing']['productGroupId'] = data['dataPricing']['groupNumber']
        simulator2pricing['productPricing']['deterioration'] = data['dataPricing']['deterioration']
        simulator2pricing['productPricing']['rates'] = data['dataPricing']['rates']
        simulator2pricing['productPricing']['groupNumber'] = data['dataPricing']['groupNumber']
        simulator2pricing['totalActivos'] = data['totalActivos']
        simulator2pricing['estrato'] = data['nomEstrato']
        if data['conCompra'] == True:
            simuladorVersion['idLineaCredito'] = 4
            cartera = compra
            cartera['monto'] = str(data['compraCartera'])
            simuladorVersion['carteras'].append(cartera)
        return simulator2pricing
    else:
        simulator2['idPagaduria'] = data['idPagaduria']
        simulator2['idOficina'] = data['idOficina']
        simulator2['actividadCliente'] = data['actividadEconomica']
        simulator2['tasa'] = data['tasa']
        simulator2['plazo'] = data['plazo']
        simulator2['monto'] = data['montoSolicitado']
        simulator2['ingresos'] = data['totalIngresos']
        simulator2['cliente']['identificacion'] = data['identificacion']
        simulator2['cliente']['fechaNacimiento'] = data['fechaNacimiento']
        simulator2['descuentosLey'] = data['descuentosLey']
        simulator2['descuentosNomina'] = data['descuentosNomina']
        simulator2['departamento'] = data['departamento']
        simulator2['genero'] = data['genero']
        simulator2['nivelEducativo'] = data['nivelEducacion']
        simulator2['totalActivos'] = data['totalActivos']
        if data['conCompra'] == True:
            simuladorVersion['idLineaCredito'] = 4
            cartera = compra
            cartera['monto'] = str(data['compraCartera'])
            simuladorVersion['carteras'].append(cartera)
        return simulator2

complementoPricingSim2 = {
    "idCredito": 338919,
    "idLineaCredito": 1,
    "idPagaduria": 190,
    "idOficina": 148,
    "actividadCliente": "DOCENTE",
    "tasa": 2.25,
    "plazo": 84,
    "monto": 20940000,
    "diasInteresesIniciales": 120,
    "ingresos": 3140000,
    "descuentosNomina": 260000,
    "descuentosLey": 147000,
    "cliente": {
        "identificacion": "1059910683",
        "fechaNacimiento": "1979-08-21"
    },
    "carteras": [],
    "departamento": "CO>Caldas",
    "genero": "M",
    "nivelEducativo": "null",
    "totalActivos": 0,
    "idAsesor": 2895
}

finSimulacion = {
    "idCredito": 0,
    "idLineaCredito": 0,
    "idPagaduria": 0,
    "idOficina": 0,
    "actividadCliente": "",
    "tasa": 0,
    "plazo": 0,
    "monto": 0,
    "diasInteresesIniciales": 120,
    "ingresos": 0,
    "descuentosNomina": 0,
    "descuentosLey": 0,
    "cliente": {
        "identificacion": "",
        "fechaNacimiento": ""
    },
    "carteras": [],
    "departamento": "",
    "genero": "",
    "nivelEducativo": "null",
    "tipoContrato": "",
    "totalActivos": 0,
    "idAsesor": 2895
}

finSimulacionPricing = {
    "idCredito": 0,
    "idLineaCredito": 0,
    "idPagaduria": 0,
    "idOficina": 0,
    "actividadCliente": "",
    "tasa": 0,
    "plazo": 0,
    "monto": 0,
    "diasInteresesIniciales": 120,
    "ingresos": 0,
    "descuentosNomina": 0,
    "descuentosLey": 0,
    "cliente": {
        "identificacion": "",
        "fechaNacimiento": ""
    },
    "carteras": [],
    "departamento": "",
    "genero": "",
    "nivelEducativo": "",
    "tipoContrato": "",
    "productPricing": {
        "rate": 0,
        "suretyBond": 0,
        "creditStudy": 0,
        "productGroupId": 0,
        "deterioration": 0,
        "rates": [],
        "groupNumber": 0
    },
    "totalActivos": 0,
    "estrato": "",
    "idAsesor": 2895
}

def finalSimulacion(data):
    if data['isPricing'] == True:
        finSimulacionPricing['idPagaduria'] = data['idPagaduria']
        finSimulacionPricing['idOficina'] = data['idOficina']
        finSimulacionPricing['actividadCliente'] = data['actividadEconomica']
        finSimulacionPricing['tasa'] = data['dataPricing']['rate']
        finSimulacionPricing['plazo'] = data['plazo']
        finSimulacionPricing['monto'] = data['montoSolicitado']
        finSimulacionPricing['ingresos'] = data['totalIngresos']
        finSimulacionPricing['descuentosNomina'] = data['descuentosNomina']
        finSimulacionPricing['descuentosLey'] = data['descuentosLey']
        finSimulacionPricing['cliente']['identificacion'] = data['identificacion']
        finSimulacionPricing['cliente']['fechaNacimiento'] = data['fechaNacimiento']
        finSimulacionPricing['departamento'] = data['departamento']
        finSimulacionPricing['genero'] = data['genero']
        finSimulacionPricing['nivelEducativo'] = data['nivelEducacion']
        finSimulacionPricing['tipoContrato'] = data['tipoContrato']
        finSimulacionPricing['totalActivos'] = data['totalActivos']
        finSimulacionPricing['estrato'] = data['nomEstrato']
        finSimulacionPricing['productPricing']['rate'] = data['dataPricing']['rate']
        finSimulacionPricing['productPricing']['suretyBond'] = data['dataPricing']['suretyBond']
        finSimulacionPricing['productPricing']['creditStudy'] = data['dataPricing']['creditStudy']
        finSimulacionPricing['productPricing']['productGroupId'] = data['dataPricing']['productGroupId']
        finSimulacionPricing['productPricing']['groupNumber'] = data['dataPricing']['groupNumber']
        finSimulacionPricing['productPricing']['deterioration'] = data['dataPricing']['deterioration']
        finSimulacionPricing['productPricing']['rates'] = data['dataPricing']['rates']
        return finSimulacionPricing
    else:
        finSimulacion['idPagaduria'] = data['idPagaduria']
        finSimulacion['idOficina'] = data['idOficina']
        finSimulacion['actividadCliente'] = data['actividadEconomica']
        finSimulacion['tasa'] = data['tasa']
        finSimulacion['plazo'] = data['plazo']
        finSimulacion['monto'] = data['montoSolicitado']
        finSimulacion['ingresos'] = data['totalIngresos']
        finSimulacion['descuentosNomina'] = data['descuentosNomina']
        finSimulacion['descuentosLey'] = data['descuentosLey']
        finSimulacion['cliente']['identificacion'] = data['identificacion']
        finSimulacion['cliente']['fechaNacimiento'] = data['fechaNacimiento']
        finSimulacion['departamento'] = data['departamento']
        finSimulacion['genero'] = data['genero']
        # finSimulacion['nivelEducativo'] = data['nivelEducacion']
        finSimulacion['tipoContrato'] = data['tipoContrato']
        finSimulacion['totalActivos'] = data['totalActivos']
        return finSimulacion

seguAp = {
    "idCredito": 0,
    "id_cliente": 0,
    "id_paquete_seguro": 0,
    "id_usuario_crea": 2895,
    "cliente_es_tomador": True,
    "beneficiariosSeguro": [
        {
            "nombres_apellidos": "prince stuart I",
            "parentesco": "primo",
            "porcentaje_asignado": 100
        }
    ]
}

def apChoise (data):
    seguAp['id_paquete_seguro'] = data['plan']
    return seguAp

referencias = [
    {
        "idCredito": 0,
        "primerNombre": "Edgar",
        "segundoNombre": "Allan",
        "primerApellido": "Poe",
        "segundoAPellido": "QA",
        "relacion": "AMIGO",
        "telefonoCelular": "3366998522",
        "departamentoTrabajo": "CO>Indefinido>Indefinido",
        "ciudadTrabajo": "CO>Indefinido>Indefinido",
        "tipoReferencia": "PERSONAL"
    },
    {
        "idCredito": 0,
        "primerNombre": "Arthur",
        "segundoNombre": "Conan ",
        "primerApellido": "Doyle",
        "segundoAPellido": "QA",
        "relacion": "ABUELO",
        "telefonoCelular": "302 205 18 00",
        "departamentoTrabajo": "CO>Indefinido>Indefinido",
        "ciudadTrabajo": "CO>Indefinido>Indefinido",
        "tipoReferencia": "FAMILIAR"
    }
]


beneficiarios = [
    {
        "idCredito": 0,
        "nombre": "prince stuart II",
        "identificacion": "25846952",
        "tipoDocumento": "CC",
        "celular": "3330201040",
        "idDepartamento": "CO>Bogotá D.C",
        "idCiudad": "CO>Bogotá D.C>BOGOTA",
        "porcentaje": 100
    }
]


peps = {
    "idCredito": 0,
    "funcionarioPublico": False,
    "manejoRecursosPublicos": False,
    "expuestoPoliticamente": False,
    "familiarExpuestoPoliticamente": False,
    "fechaVinculacion": "",
    "familiares": []
}

oi = {
    "idCredito": 0,
    "tieneTransaccionExtranjera": False,
    "productoBancario": {
        "tieneProducto": False
    }
}



# data = cl.dataSimulador()
# # print(data)
# print(dataSimulador(data=data))





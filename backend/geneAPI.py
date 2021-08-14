import re
import os
import ast
import boto3
import logging
import pymongo as pm
import psycopg2 as pypg
from bottle_jwt import auth
from botocore.config import Config
from bson.objectid import ObjectId
from models.latlong import LatLong
from models.distance import MetricDistance
from operations.calculate import Calculations
from operations.misc_ops import OtherOperations
from operations.corroboration import Corroboration
from truckpad.bottle.cors import CorsPlugin, enable_cors
from bottle import Bottle, request, response, post, get, put, delete, run
app = Bottle(__name__)
emailpattern = re.compile(r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
passwordpattern = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
mop = OtherOperations()
calc = Calculations()
# print("++++++++++++++++++++++++++++++++++++++++")
# print(MetricDistance(Calculations().haversine(
#     LatLong(12.9739697, 80.2151917), LatLong(12.9794559, 80.2222834))))
# print("-----------------------------------------")
# exit()


# '''update public.diseases set disease=%s , disease_category_id= %s, disease_image_url=%s where disease_id=%s'''
# cqs+
# cur.execute('''insert into public.registered_users(user_name, user_mail, pincode, password) values (%s , %s )''', ())
# @app.delete
# @app.
# @app.
# @app.
# @app.
# ast.literal_eval(request.body.read().decode('utf8'))
# ud1 = (data['password'],
#        data['date_of_birth'], data['gender'], data['user_email'], data['mobile_number'], data['user_name'])
# (, KeyError)
# where where


mc = pm.MongoClient("mongodb://localhost:27017")
db = mc['local']
col = db['gene_test_results']
con = pypg.connect(user='postgres', password='password', database='postgres')
cur = con.cursor()

# mys = boto3.session.Session(
#     aws_access_key_id='AKIA4NWNR6RKLLQXECEN', aws_secret_access_key='DsspNdp62GLSoK2xDLrSPaQyqW7Wz1iK92iL2h', region_name='ap-south-1')
# myr = mys.region_name
# client = mys.client('s3', aws_access_key_id='AKIA4NWNR6RKLLQXECEN', aws_secret_access_key='DsspNdp62GLSoK2xDLrSPaQyqW7Wz1iK92iL2h',
#                     region_name='ap-south-1', config=Config(signature_version='s3v4'))
# s3 = boto3.resource('s3')
# for bucket in s3.buckets.all():
#     print(bucket.name)


@app.post('/login')
@enable_cors
def login():
    try:
        try:
            data = request.json if request.json is not None else ast.literal_eval(
                request.body.read().decode('utf8'))
        except:
            raise ValueError

        if data is None:
            raise ValueError
        try:
            cs = ''''''
            dts = ''''''
            ids = ''''''
            b = 0
            ud = []
            if ((('user_email' in data.keys() and 'password' in data.keys() and 'mobile_number' not in data.keys()) or ('user_email' not in data.keys() and 'password' not in data.keys() and 'mobile_number' in data.keys())) and 'device_token' in data.keys()):
                if 'mobile_number' in data.keys() and 'device_token' in data.keys():
                    cs = '''select count(user_id) from public.registered_users where mobile_number = %s'''
                    ud = (data['mobile_number'], )
                    dts = '''select device_token from public.registered_users where mobile_number=%s'''
                    ids = '''select user_id from public.registered_users where mobile_number=%s'''
                elif 'user_email' in data.keys() and 'password' in data.keys() and 'device_token' in data.keys():
                    cs = '''select count(user_id) from public.registered_users where user_email=%s and password=%s'''
                    ud = (data['user_email'], data['password'])
                    dts = '''select device_token from public.registered_users where user_email=%s and password=%s'''
                    ids = '''select user_id from public.registered_users where user_email=%s and password=%s'''
                cur.execute(cs, ud)
                a = cur.fetchone()[0]
                if a == 1:
                    cur.execute(ids, ud)
                    uid = cur.fetchone()[0]
                    cur.execute(dts, ud)
                    dt = cur.fetchone()[0]
                    if len(dt) == 0:
                        cur.execute(
                            '''update public.registered_users set device_token=%s where user_id=%s''', (data['device_token'], uid))
                        con.commit()
                        cur.execute(
                            '''select user_type_id from public.registered_users where user_id=%s''', (uid,))
                        b = cur.fetchone()[0]
                        response.body = str(
                            {"success": True, "status": True, "message": "Logged in Successfully", "user_type": b})

                    elif dt == data['device_token']:
                        cur.execute(
                            '''select user_type_id from public.registered_users where user_id=%s''', (uid,))
                        b = cur.fetchone()[0]
                        response.body = str(
                            {"success": True, "status": True, "message": "Logged in Successfully", "user_type": b})
                    else:
                        response.body = str(
                            {"success": True, "status": False, "message": "User is Already Logged In"})
                else:
                    response.body = str(
                        {"success": True, "status": False, "message": "User is not Registered"})
            else:
                raise KeyError
        except TypeError:
            raise ValueError

    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        if ('user_email' in data.keys() or 'password' in data.keys()) and 'mobile_number' in data.keys():
            response.body = str(
                {"success": False, "status": False, "message": "Ambiguous Login"})
        elif 'user_email' in data.keys() and data['user_email'] != "" and 'password' not in data.keys() and 'device_token' not in data.keys() and 'mobile_number' not in data.keys():
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide Password and Device Token"})
        elif 'password' in data.keys() and data['password'] != "" and 'user_email' not in data.keys() and 'device_token' not in data.keys() and 'mobile_number' not in data.keys():
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide Email and Device Token"})
        elif mop.logicalXOR('user_email' in data.keys() and data['user_email'] != "" and 'password' in data.keys() and data['password'] != "", 'mobile_number' in data.keys() and data['mobile_number'] != "") and 'device_token' not in data.keys():
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide Device Token"})
        elif 'device_token' in data.keys() and data['device_token'] != "" and not(mop.logicalXOR(('user_email' in data.keys() and 'password' in data.keys()), 'mobile_number' in data.keys())):
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide either Email and Password or Mobile Number"})
        else:
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide The Necessary Parameters"})
        return ast.literal_eval(response.body)
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@ app.post('/register')
@ enable_cors
def register():
    try:
        try:
            data = request.json if request.json is not None else ast.literal_eval(
                request.body.read().decode('utf8'))
        except:
            raise ValueError
        if data is None or data == {}:
            raise ValueError
        try:
            if 'user_name' in data.keys() and 'password' in data.keys() and 'user_type' in data.keys() and 'user_email' in data.keys() and 'pincode' in data.keys() and 'gender' in data.keys() and 'mobile_number' in data.keys() and 'country' in data.keys() and emailpattern.match(data['user_email']) != None and passwordpattern.match(data['password']) != None:
                ud = (data['user_name'], data['user_type'],
                      data['user_email'], data['password'], data['mobile_number'])
                cs = mop.generateCountStatement(
                    'public.registered_users', data, 'user_id')
                cur.execute(cs, ud)
                if cur.fetchone()[0] == 0:
                    try:
                        ao = LatLong()
                        x = ao.getLatLongFromZipCodeAndCountryCode(
                            data['pincode'], data['country'])
                        user_data = (data['user_name'],
                                     data['user_type'], data['date_of_birth'], data['gender'], data['mobile_number'], data['user_email'], x['latitude'], x['longitude'], data['password'])
                        cur.execute(
                            '''insert into public.registered_users(user_name, user_type_id, date_of_birth, gender_id, mobile_number, user_email, latitude, longitude, password) values(%s , %s , %s , %s , %s , %s , %s , %s , %s)''', user_data)
                        con.commit()
                        cur.execute(
                            '''select user_id from public.registered_users where user_name=%s and user_type=%s and date_of_birth=%s and gender=%s and mobile_number=%s and user_email=%s and latitude=%s and longitude=%s and password=%s''', user_data)
                        b = cur.fetchone()[0]
                        response.body = str(
                            {"success": True, "status": True, "message": "User Registered Successfully", "user_id": b})
                    except Exception as e:
                        error = e.args[0].split('\n')[0]
                        response.body = str(
                            {"success": False, "status": False, "message": error})
                else:
                    response.body = str(
                        {"success": True, "status": True, "message": "User is Already Registered, Please Login"})
        except (TypeError, KeyError):
            raise ValueError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/userDetails')
@enable_cors
def getUserDetails():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'device_token' in data.keys():
            try:
                q = mop.getListFromDict(data)
                cur.execute(
                    '''select U.user_name, T.user_type, U.date_of_birth, G.gender, U.mobile_number, U.user_email, U.latitude, U.longitude from public.registered_users U inner join public.genders G on U.gender_id = G.gender_id inner join public.user_types T on U.user_type_id = T.user_type_id and U.device_token=%s''', q)
                dft = [dict(zip([col[0] for col in cur.description], row))
                       for row in cur]
                if dft is not None and dft != []:
                    fd = dft[0]
                    fd['date_of_birth'] = fd['date_of_birth'].strftime(
                        "%Y-%m-%d %H:%M:%S")
                    response.body = str(
                        {"success": True, "status": True, "message": "User Details", "result": str(fd)})
                else:
                    response.body = str(
                        {"success": True, "status": True, "message": "User Details"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    rb = ast.literal_eval(response.body)
    result = ast.literal_eval(rb['result']) if 'result' in rb.keys() else None
    if result is not None:
        rb['result'] = result
    return rb


@app.put('/updateUserDetails')
@enable_cors
def updateUserData():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'device_token' in data.keys():
            cqs = mop.generateUpdateStatement('public.registered_users', data)
            ud2 = mop.getListFromDict(data)
            try:
                cur.execute(cqs, ud2)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "User Details Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError

    except ValueError:
        response.status = 400
        return
    except KeyError as e:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteUser')
@enable_cors
def deleteUser():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'device_token' in data.keys():
            try:
                cur.execute(
                    '''delete from public.registered_users where device_token=%s''', (data['device_token'],))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "User Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/storeDocs')
@enable_cors
def storeDocs():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'user_id' in data.keys() and 'doc_type' in data.keys() and 'doc_url' in data.keys():
            try:
                cur.execute(
                    '''insert into public.documents(user_id, doc_type, doc_url) values(%s,%s,%s)''', (data['user_id'], data['doc_type'], data['doc_url']))
                con.commit()
                cur.execute(
                    '''select doc_id from public.documents where user_id=%s and doc_type=%s and doc_url=%s''', (data['user_id'], data['doc_type'], data['doc_url']))
                a = cur.fetchone()[0]
                response.body = str(
                    {"success": True, "status": True, "message": "Document Uploaded Successfully", "doc_id": a})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteDoc')
@enable_cors
def deleteDocument():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'doc_id' in data.keys():
            try:
                cur.execute(
                    '''delete from public.documents where doc_id=%s''', (data['doc_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Document Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addDiseaseCategory')
@enable_cors
def addDiseaseCategory():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'disease_category' in data.keys() and 'user_type' in data.keys():
            try:
                dt = (data['disease_category'].lower(),)
                cur.execute(
                    '''select count(disease_category_id) from public.disease_categories where disease_category=%s''', dt)
                b = cur.fetchone()[0]
                if data['user_type'] in (1, 2):
                    if b == 0:
                        try:
                            cur.execute(
                                '''insert into public.disease_categories(disease_category) values(%s)''', dt)
                            con.commit()
                            cur.execute(
                                '''select disease_category_id from public.disease_categories where disease_category=%s''', (data['disease_category'],))
                            c = cur.fetchone()[0]
                            response.body = str(
                                {"success": True, "status": True, "message": "Disease Category Added Successfully", "disease_category_id": c})
                        except Exception as e:
                            error = e.args[0].split('\n')[0]
                            response.body = str(
                                {"success": False, "status": False, "message": error})
                    else:
                        response.body = str(
                            {"success": True, "status": True, "message": "Disease Category is Already Added"})
                else:
                    response.body = str(
                        {"success": False, "status": False, "message": "You are restricted from Adding Disease Category"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateDiseaseCategory')
@enable_cors
def updateDiseaseCategory():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data == {} or data is None:
            raise ValueError
        elif 'disease_category' in data.keys() and 'disease_category_id' in data.keys():
            try:
                cur.execute(
                    '''update public.disease_categories set disease_category = %s where disease_category_id = %s''', (data['disease_category'], data['disease_category_id']))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Category Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteDiseaseCategory')
@enable_cors
def deleteDiseaseCategory():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'disease_category_id' in data.keys():
            try:
                cur.execute(
                    '''delete from public.disease_categories where disease_category_id = %s''', (data['disease_category_id'],))
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Category Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addDisease')
@enable_cors
def addDisease():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'disease' in data.keys() and 'disease_image_url' in data.keys() and 'user_type' in data.keys():
            try:
                d1 = (data['disease'].lower(), data['disease_image_url'])
                d2 = (data['disease'].lower(),)
                cur.execute(
                    '''select count(disease_id) from public.diseases where disease=%s''', d2)
                f = cur.fetchone()[0]
                if data['user_type'] in (1, 2):
                    if f == 0:
                        try:
                            cur.execute(
                                '''insert into public.diseases(disease_category_id,disease,disease_image_url) values (%s,%s,%s)''', d1)
                            con.commit()
                            cur.execute(
                                '''select disease_id from public.diseases where disease=%s''', d2)
                            w = cur.fetchone()[0]
                            response.body = str(
                                {"success": True, "status": True, "message": "Disease Added Successfully", "disease_id": w})
                        except Exception as e:
                            error = e.args[0].split('\n')[0]
                            response.body = str(
                                {"success": False, "status": False, "message": error})
                    else:
                        response.body = str(
                            {"success": True, "status": True, "message": "Disease Already Added"})
                else:
                    response.body = str(
                        {"success": False, "status": False, "message": "You are restricted from Adding Disease"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        if 'disease' not in data.keys() and 'disease_image_url' in data.keys():
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide Disease Name"})
        elif 'disease_image_url' not in data.keys() and 'disease' in data.keys():
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide Disease Image"})
        else:
            response.body = str(
                {"success": False, "status": False, "message": "Please Provide The Necessary Parameters"})
        return ast.literal_eval(response.body)

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateDisease')
@enable_cors
def updateDisease():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'disease_id' in data.keys() and 'disease' in data.keys() and 'disease_category_id' in data.keys() and 'disease_image_url' in data.keys():
            try:
                d1 = (data['disease'], data['disease_category_id'], data['disease_image_url'],
                      data['disease_id'])
                qs = mop.generateUpdateStatement('public.diseases', data)
                cur.execute(qs, d1)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteDisease')
@enable_cors
def deleteDisease():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'disease_id' in data.keys():
            try:
                a = (data['disease_id'],)
                cur.execute(
                    '''delete from public.diseases where disease_id=%s''', a)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Disease Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addGene')
@enable_cors
def addGene():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'gene' in data.keys() and 'user_type' in data.keys():
            try:
                dt = (data['gene'].upper(), )
                cur.execute(
                    '''select count(gene_id) from public.genes where gene=%s''', dt)
                c = cur.fetchone()[0]
                if data['user_type'] in (1, 2):
                    if c == 0:
                        try:
                            cur.execute(
                                '''insert into public.genes(gene) values(%s)''', dt)
                            con.commit()
                            cur.execute(
                                '''select gene_id from public.genes where gene=%s''', dt)
                            d = cur.fetchone()[0]
                            response.body = str(
                                {"success": True, "status": True, "message": "Gene Added Successfully", "gene_id": d})
                        except Exception as e:
                            error = e.args[0].split('\n')[0]
                            response.body = str(
                                {"success": False, "status": False, "message": error})
                    else:
                        response.body = str(
                            {"success": True, "status": True, "message": "Gene Added Already"})
                else:
                    response.body = str(
                        {"success": False, "status": False, "message": "You are restricted from Adding Gene"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/storeResult')
@enable_cors
def storeResult():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'patient_id' in data.keys() and 'patient_gene_id' in data.keys() and 'molecular_value' in data.keys() and 'biological_process' in data.keys() and 'cellular_component' in data.keys() and 'molecular_value_average' in data.keys() and 'biological_process_average' in data.keys() and 'cellular_component_average' in data.keys() and 'cross_ontology_value' in data.keys() and 'cross_ontology_result' in data.keys() and 'possible_disease_id' in data.keys() and 'possible_disease Name' in data.keys() and 'pharmatist_id' in data.keys() and 'symptoms' in data.keys() and 'preventive_measures' in data.keys():
            try:
                upd = col.insert_one(data)
                id = str(upd.inserted_id)
                utd = (data['patient_id'], id)
                cur.execute(
                    '''insert into public.user_test_results values(%s,%s)''', utd)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Result Stored Successfully", "result_id": id})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        response.body = str({"success": False, "status": False, "message": ""})
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateGene')
@enable_cors
def updateGene():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data == {} or data is None:
            raise ValueError
        elif 'gene' in data.keys() and 'gene_id' in data.keys():
            try:
                gd = (data['gene'], data['gene_id'])
                qs = mop.generateUpdateStatement('public.genes', data)
                cur.execute(qs, gd)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Gene Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteGene')
@enable_cors
def deleteGene():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'gene_id' in data.keys():
            try:
                p = (data['gene_id'],)
                cur.execute('''delete from public.genes where gene_id=%s''', p)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Gene Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/addSymptom')
@enable_cors
def addSymptom():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data == {} or data is None:
            raise ValueError
        elif 'symptom' in data.keys() and 'user_type' in data.keys():
            if data['user_type'] in (1, 2):
                try:
                    a = (data['symptom'],)
                    cur.execute(
                        '''insert into public.symptoms(symptom) values(%s)''', a)
                    con.commit()
                    response.body = str(
                        {"success": True, "status": True, "message": "Symptom Added Successfully"})
                except Exception as e:
                    error = e.args[0].split('\n')[0]
                    response.body = str(
                        {"success": False, "status": False, "message": error})
            else:
                response.body = str(
                    {"success": False, "status": False, "message": "You are restricted from Adding Symptoms"})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.put('/updateSymptom')
@enable_cors
def updateSymptom():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'symptom' in data.keys() and 'symptom_id' in data.keys():
            try:
                sd = (data['symptom'], data['symptom_id'])
                qs = mop.generateUpdateStatement('public.symptoms', data)
                cur.execute(qs, sd)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Symptom Updated Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.delete('/deleteSymptom')
@enable_cors
def deleteSymptom():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'symptom_id' in data.keys():
            try:
                v = (data['symptom_id'],)
                cur.execute(
                    '''delete from public.symptoms where symptom_id=%s''', v)
                con.commit()
                response.body = str(
                    {"success": True, "status": True, "message": "Symptom Deleted Successfully"})
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return
    except KeyError:
        response.status = 409
        return

    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    return ast.literal_eval(response.body)


@app.post('/getDocumentList')
@enable_cors
def getDocumentList():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'device_token' in data.keys():
            try:
                cur.execute(
                    '''select D.doc_id,D.doc_type, D.doc_url from public.documents D left join public.registered_users U on D.user_id = U.user_id and U.device_token=%s''', (data['device_token'],))
                d = [dict(zip([col[0] for col in cur.description], row))
                     for row in cur]
                b = {"success": True, "status": True,
                     "message": "Document List", "result": str(d)}
                response.body = str(b)
            except Exception as e:
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    rb = ast.literal_eval(response.body)
    result = ast.literal_eval(rb['result']) if 'result' in rb.keys() else None
    if result is not None:
        rb['result'] = result
    return rb


@app.post('/getPatientsList')
@enable_cors
def getPatientsList():
    try:
        cur.execute('''select U.user_name, U.date_of_birth, G.gender, U.mobile_number, U.user_email, U.pincode from public.registered_users U inner join genders G on U.gender_id = G.gender_id and user_type_id=%s''', ("0",))
        d = [dict(zip([col[0] for col in cur.description], row))
             for row in cur]
        for i in d:
            i['date_of_birth'] = i['date_of_birth'].strftime(
                "%Y-%m-%d %H:%M:%S")
        b = {"success": True, "status": True,
             "message": "Patient List", "result": str(d)}
        response.body = str(b)
    except Exception as e:
        error = e.args[0].split('\n')[0]
        response.body = str(
            {"success": False, "status": False, "message": error})
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    rb = ast.literal_eval(response.body)
    result = ast.literal_eval(rb['result']) if 'result' in rb.keys() else None
    if result is not None:
        rb['result'] = result
    return rb


@app.post('/searchDiseases')
@enable_cors
def getSearchedDiseases():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'pattern' in data.keys():
            try:
                sdt = ('''%%''' + data['pattern'] + '''%%''',)
                cur.execute(
                    '''select disease_id,disease,disease_image_url from public.diseases where disease like %s''', sdt)
                d = [dict(zip([col[0] for col in cur.description], row))
                     for row in cur]
                b = {"success": True, "status": True,
                     "message": "Disease List", "result": str(d)}
                response.body = str(b)
            except Exception as e:
                print(e)
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    rb = ast.literal_eval(response.body)
    result = ast.literal_eval(rb['result']) if 'result' in rb.keys() else None
    if result is not None:
        rb['result'] = result
    return rb


@app.post('/getTestResults')
@enable_cors
def getTestResults():
    try:
        data = request.json if request.json is not None else ast.literal_eval(
            request.body.read().decode('utf8'))
        if data is None or data == {}:
            raise ValueError
        elif 'device_token' in data.keys():
            try:
                cur.execute(
                    '''select R.result_id from public.user_test_results R left join public.registered_users U on R.user_id = U.user_id and U.device_token=%s''', (data['device_token'],))
                a = cur.fetchall()
                res = []
                for i in a:
                    c = col.find_one({'_id': ObjectId(i[0])})
                    d = 0
                    if c != None:
                        d = c.pop('_id', None)
                        res.append(c)
                b = {"success": True, "status": True,
                     "message": "Test Results List", "result": str(res)}
                response.body = str(b)
            except Exception as e:
                print(e)
                error = e.args[0].split('\n')[0]
                response.body = str(
                    {"success": False, "status": False, "message": error})
        else:
            raise KeyError
    except ValueError:
        response.status = 400
        return

    except KeyError:
        response.status = 409
        return
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    response.headers['Content-Type'] = 'application/json'
    rb = ast.literal_eval(response.body)
    result = ast.literal_eval(rb['result']) if 'result' in rb.keys() else None
    if result is not None:
        rb['result'] = result
    return rb


@app.post('/logout')
@enable_cors
def logout():
    try:
        data = ast.literal_eval(
            request.body.read().decode('utf8')) if request.json is None else request.json
        sqs = mop.generateSelectStatement(
            'public.registered_users', ['user_id'], data)
        ldt = mop.getListFromDict(data)
        cur.execute(sqs, ldt)
        uid = cur.fetchone()[0]
        udt = ("", uid)
        cur.execute(
            '''update public.registered_users set device_token=%s where user_id=%s''', udt)
        con.commit()
        response.body = str(
            {"success": True, "status": True, "message": "Logged out Successfully"})
    except Exception as e:
        error = e.args[0].split('\n')[0]
        print(e.args)
        response.body = str(
            {"success": False, "status": False, "message": error})
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    return ast.literal_eval(response.body)


if __name__ == "__main__":
    app.install(CorsPlugin(
        origins=['http://localhost:8080/#/', 'http://localhost:8080/', 'http://localhost:8080']))
    app.run(host='127.0.0.1', port='8000', reloader=True, debug=True)

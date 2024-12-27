# =========== Khai báo biến sử dụng ====================
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.clearcolor = (0.9,0.9,0.9,1) # Window Background clolor 

# ========= Hàm định dạng hiển thị ====================
class MyGrid(GridLayout):
	def __init__(self, **kwargs):
		super(MyGrid,self).__init__(**kwargs)

		# Định dạng hiển thị 1 cột
		self.cols = 1

		# Hiển thị tên App
		self.add_widget(Label(text = '* GIẢI MÃ ENIGMA *', size= (300,50), size_hint= (1,None), font_size = 25, color= [0, 0, 0, 1]))

		# Hiển thị cảnh báo bản quyền App
		self.add_widget(Label(text = '* Bản quyền thuộc về DUTIAN Việt Nam *', size= (300,1), size_hint= (1,None), font_size = 15, color= [0.5, 0.2, 0.8, 1]))

		# Hiển thị label khoảng trống
		self.add_widget(Label( size= (250,20), size_hint= (None,None), font_size = 15))

		# Hiển thị cảnh báo chia sẻ App
		self.add_widget(Label(text = '- Vui lòng không chia sẻ dưới mọi hình thức -', size= (300,5), size_hint= (1,None), font_size = 15, color= [1, 0, 0, 1]))

		# Hiển thị label khoảng trống
		self.add_widget(Label( size= (250,20), size_hint= (None,None), font_size = 15))

		# Hiển thị label tên quản trị viên
		self.add_widget(Label(text = 'Tên Admin : ', size= (99,35), size_hint= (None,None), font_size = 15, color= [0, 0, 0, 1]))

		# Hiển thị ô nhập tên quản trị viên
		self.Ten_quan_tri_vien_input  = TextInput(size= (250,35),size_hint= (None,None), font_size = 15, multiline = False, password = 'true', password_mask = '*')
		self.add_widget(self.Ten_quan_tri_vien_input)

		# Hiển thị label mật khẩu
		self.add_widget(Label(text = 'Mật khẩu : ', size= (88,38), size_hint= (None,None), font_size = 15, color= [0, 0, 0, 1]))

		# Hiển thị ô nhập mật khẩu
		self.Password_input  = TextInput(size= (250,35),size_hint= (None,None), font_size = 15, multiline = False, password = 'true', password_mask = '*')
		self.add_widget(self.Password_input)

		# Hiển thị label mã bảo mật
		self.add_widget(Label(text = 'Key giải mã : ', size= (103,38), size_hint= (None,None), font_size = 15, color= [0, 0, 0, 1]))

		# Hiển thị ô nhập mã bảo mật
		self.Security_input  = TextInput(size= (250,35),size_hint= (None,None), font_size = 15, multiline = False, password = 'true', password_mask = '*')
		self.add_widget(self.Security_input)

		# Hiển thị label khoảng trống
		self.add_widget(Label( size= (250,25), size_hint= (None,None), font_size = 15))

		# Hiển thị label mã khách hàng
		self.add_widget(Label(text = 'Mã từ khách hàng :', size= (140,35), size_hint= (None,None), font_size = 15, color= [0, 0, 0, 1]))

		# Hiển thị ô nhập mã người dùng
		self.Ma_nguoi_dung_input  = TextInput(size= (250,35),size_hint= (1,None), font_size = 12, multiline = False)
		self.add_widget(self.Ma_nguoi_dung_input)

		# Hiển thị label khoảng trống
		self.add_widget(Label( size= (250,25), size_hint= (None,None), font_size = 15))

		# Hiển thị label kết quả
		self.add_widget(Label(text = 'Kết quả sau giải mã :', size= (155,35), size_hint= (None,None), font_size = 15, color= [0, 0, 0, 1]))

		# Hiển thị ô hiển thị kết quả
		self.Ket_qua_input  = TextInput(size= (250,35),size_hint= (1,None), font_size = 12, multiline = False, readonly = 'true')
		self.add_widget(self.Ket_qua_input)

		# Hiển thị khoảng trống
		self.add_widget(Label( size= (250,25), size_hint= (None,None), font_size = 15))
		self.add_widget(Label( size= (250,25), size_hint= (None,None), font_size = 15))

		# Hiển thị nút nhấn thực thi giải mã
		self.Activation = Button(text = 'TIẾN HÀNH GIẢI MÃ', size= (500,75), size_hint= (1,None), font_size = 15,background_color = [0, 0,0.7, 0.5])
		self.Activation.bind(on_press = self.pressed)
		self.add_widget(self.Activation)

		# Hiển thị bảng End
		self.End = Button(size= (500,100), size_hint= (1,1), background_color = [1, 1, 1, 0.3])
		self.add_widget(self.End)

# ===== Sự kiện nhấn nút giải mã ================
	def pressed(self,instance):
		admin_name      = self.Ten_quan_tri_vien_input.text 
		admin_pass      = self.Password_input.text
		admin_security  = self.Security_input.text
		User_code       = self.Ma_nguoi_dung_input.text

		sai_ten ='false'
		sai_mat_khau ='false'
		sai_ma_bao_mat ='false'
		chua_nhap_ma_khach_hang ='false'
		self.Ket_qua_input.text = ''

		if((admin_name == 'quangtrumbk' or admin_name == 'thanhitreetek') and (admin_pass == '@Dutian*' or admin_pass == '@itreetek*') and (admin_security == '*#01245ACD9763F@*') and (User_code != '')):

			# Đảo chuỗi người dùng
			revert_User_code = User_code[::-1]

			# Nối thêm chuỗi
			Add_User_code = 'acbe' + revert_User_code + 'GDFH'

			# Chuyển thành Hexa
			Hexa_User_code = Add_User_code.encode('utf-8').hex()

			# Dịch sang phải 7 ký tự
			check_lengt_1 = 7 % len(Hexa_User_code)                                                       # Kiểm tra nếu n lớn hơn độ dài chuỗi
			shift_right_User_code_1 = Hexa_User_code[-check_lengt_1:] + Hexa_User_code[:-check_lengt_1]   # Dịch chuỗi sang phải

			# Tách số trong chuỗi
			Digit_User_code = [char for char in shift_right_User_code_1 if char.isdigit()]

			# Dịch sang phải 8 ký tự
			check_lengt_2 = 8 % len(Digit_User_code)                                                      # Kiểm tra nếu n lớn hơn độ dài chuỗi
			shift_right_User_code_2 = Digit_User_code[-check_lengt_2:] + Digit_User_code[:-check_lengt_2] # Dịch chuỗi sang phải

			# Ghép ký tự riêng biệt trong chuỗi thành 1 từ liên tục
			Join_User_code = ''.join(shift_right_User_code_2)

			# Kiểm tra độ dài chuỗi
			Check_length_user_code =len(Join_User_code)

			# Cắt chuỗi lấy 25 ký tự bắt đầu từ ký tự 01
			if(Check_length_user_code >= 27):
				Cut_User_code = Join_User_code[1:26]
			else:
				Cut_User_code = Join_User_code

			# Xuất kết quả	
			self.Ket_qua_input.text = str(Cut_User_code)
		else:

			# Check xem thông tin nào sai 
			if(admin_name != 'quangtrumbk' and admin_name != 'thanhitreetek'):
				sai_ten = 'true'

			if(admin_pass != '@Dutian*' and admin_pass != '@itreetek*'):
				sai_mat_khau ='true'

			if(admin_security != '*#01245ACD9763F@*'):
				sai_ma_bao_mat ='true'

			if(User_code == ''): 
				chua_nhap_ma_khach_hang ='true'

			# Sum thông tin sai và hiển thị kết quả đang sai gì
			if(sai_ten != 'true' and sai_mat_khau !='true' and sai_ma_bao_mat =='true'):
				self.Ket_qua_input.text = 'Sai mã bảo mật'
			if(sai_ten != 'true' and sai_mat_khau =='true' and sai_ma_bao_mat !='true'):
				self.Ket_qua_input.text = 'Sai mật khẩu'
			if(sai_ten != 'true' and sai_mat_khau =='true' and sai_ma_bao_mat =='true'):
				self.Ket_qua_input.text = 'Sai mã bảo mật' + ' , ' + 'Sai mật khẩu'
			if(sai_ten == 'true' and sai_mat_khau !='true' and sai_ma_bao_mat !='true'):
				self.Ket_qua_input.text = 'Sai tên admin'
			if(sai_ten == 'true' and sai_mat_khau !='true' and sai_ma_bao_mat =='true'):
				self.Ket_qua_input.text = 'Sai tên admin' + ' , ' + 'Sai mã bảo mật'
			if(sai_ten == 'true' and sai_mat_khau =='true' and sai_ma_bao_mat !='true'):
				self.Ket_qua_input.text = 'Sai tên admin' + ' , ' + 'Sai mật khẩu'
			if(sai_ten == 'true' and sai_mat_khau =='true' and sai_ma_bao_mat =='true'):
				self.Ket_qua_input.text = 'Sai tên admin' + ' , ' + 'Sai mật khẩu' + ' , ' + 'Sai mã bảo mật'

			if(chua_nhap_ma_khach_hang =='true'):
				self.Ket_qua_input.text = self.Ket_qua_input.text + ' , ' + "Chưa nhập mã khách hàng"

			# Reset lại biến
			sai_ten ='false'
			sai_mat_khau ='false'
			sai_ma_bao_mat ='false'
			chua_nhap_ma_khach_hang =='false'

# ============ Hàm chính =========================
class ENIGMA_DECRIPTION_APP (App):
	def build (self):
		
		self.icon = 'Logo.png'
		self.title = 'GIẢI MÃ ENIGMA'

		return MyGrid()
if __name__ == "__main__":
	ENIGMA_DECRIPTION_APP().run()

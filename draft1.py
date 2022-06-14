class myclass:
def __init__(self):
	self.poly_mod_deg;
	self.coeff_mod;
	self.scale;
	self.depth;
	…
def set_EncParameters(self, input_params):
	self.poly_mod_deg = input_params.poly_mod_deg;
	…
def create_context:
	cal_context_data();
  err_message();
	print_params();

  
context::err_message():
"""  if(	input_params.poly_mod_deg 조건(2n))?
	   [Y] max비트길이 조건내에서 소수선택하는 함수로
    input_params.coeff_mod ={p1,p2,…pD-1} 찾음.
	  [N] err
    if(	input_params.scale비크크기>coeff_mod의 p1비트길이)
	  [Y] err
   context::cal_context_data():
    파라미터 coeff_mod의 소수를 하나씩제거한 copy들을 (0~D-1)level들로 구성
"""

def keyGen(context):
개인/공개/재선형화 키만드는 함수들

input class
data=x
algorithm=”a*x^3+…..”

def encoder(self,context):
 slot_count=self.poly+mode_





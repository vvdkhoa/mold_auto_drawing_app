from pathlib import Path
import csv
import json
import os
path = os.path.dirname(os.path.abspath(__file__))
import sys
from database.database import sql_get_dict
import math

############## Get FreeCAD Lib ############
#### Read json file in database forder Use when built app #### 
now_path_g = os.path.dirname(os.path.abspath(__file__))
parent_dir_g = Path(now_path_g).parent.parent.joinpath('database') # Database Dir
FreeCAD_path = str(parent_dir_g).replace('\\', '/') + '/FreeCAD_path.json'
with open(FreeCAD_path, 'r', encoding='utf-8') as f:
	Data_dict = json.load(f)[0]
	freecad_path = Data_dict['FreeCAD_path']
#### 

#### Setting direct when code ####
# freecad_path = 'D:/Program Files/FreeCAD 0.18/bin'
#### 

print('FreeCAD path: %s' % freecad_path)
sys.path.append(freecad_path)
##############

import FreeCAD
import Import

############## Create Box #############################
class Box:
	def __init__(self, doc, name, w, h, t, x, y, z):
		self.doc = doc
		self.name = name
		self.width = w
		self.height = h
		self.thick = t
		self.x = x
		self.y = y
		self.z = z
	def create_box(self):
		box = self.doc.addObject("Part::Box",self.name)
		box.Length = self.width # xyz freecad != icad
		box.Height = self.thick # xyz freecad != icad
		box.Width = self.height # xyz freecad != icad
		myvec = FreeCAD.Vector(self.x-self.width/2 , self.y-self.height/2, self.z) # fix with icad
		box.Placement.Base = myvec

############## Cylinder #############################
class Cylinder:
	def __init__(self, doc, name, d, l, x, y, z):
		self.doc = doc
		self.name = name
		self.diameter = d/2
		self.length = l
		self.x = x
		self.y = y
		self.z = z
	def create_cylinder(self):
		cyl = self.doc.addObject("Part::Cylinder",self.name)
		cyl.Radius = self.diameter
		cyl.Height = self.length # cyl.Placement.Rotation = (0.0, 1.0, 1.0, 0.0)
		myvec = FreeCAD.Vector(self.x, self.y, self.z)
		cyl.Placement.Base = myvec

############## Cylinder #############################
# yaw: z, pitch: y, roll: x ; https://www.freecadweb.org/wiki/Placement
class AngularCylinder():
	def __init__(self, doc, name, d, l, h, x, y, z, yaw, pitch, roll):
		self.doc = doc
		self.name = name
		self.diameter = d/2
		self.length = l
		self.hight = h
		self.x = x
		self.y = y
		self.z = z
		self.yaw = yaw
		self.pitch = pitch
		self.roll = roll
	# yaw: z, pitch: y, roll: x ; https://www.freecadweb.org/wiki/Placement
	def create_angular_pin(self):
		# Create cylinder and rotate
		cyl = self.doc.addObject("Part::Cylinder",'_ag_1')
		cyl.Radius = self.diameter
		cyl.Height = self.length

		if self.pitch != 0: # Left right angular pin
			x = self.x -self.length * math.sin(math.radians(self.pitch))
			y = self.y
			z = self.z + self.hight - self.length * math.cos(math.radians(self.pitch))
		elif self.roll != 0: # Up down angular pin
			x = self.x
			y = self.y + self.length * math.sin(math.radians(self.roll))
			z = self.z + self.hight - self.length * math.cos(math.radians(self.roll))

		cyl.Placement = FreeCAD.Placement(FreeCAD.Vector(x,y,z),
									FreeCAD.Rotation(self.yaw, self.pitch, self.roll))
		# Create Sphere
		sph = self.doc.addObject("Part::Sphere",'_ag_2')
		sph.Radius =  self.diameter
		sph.Placement.Base = FreeCAD.Vector(self.x, self.y, self.z+self.hight)
		# Add Angular cylinder and Sphere
		agp = self.doc.addObject("Part::MultiFuse", self.name)
		agp.Shapes = [cyl, sph]


############## Drawing Molding Class #############################
class Molding(Box, Cylinder):

	def __init__(self):
		self.doc = self.create_doc()

		d = self.read_dimentions()
		s = self.read_settings()
		self.w1 = d['w1']
		self.w2 = d['w2']
		self.h1 = d['h1']
		self.h2 = d['h2']
		self.t1 = d['t1']
		self.t2 = d['t2']
		self.w3 = d['w3']
		self.h3 = d['h3']
		self.t3 = d['t3']
		self.o1 = d['o1'] # Product
		self.o2 = d['o2'] # Runner
		self.o3 = d['o3'] # Nozzle
		self.ej = d['ej']
		self.t_gpx = d['t_gpx']
		self.t_gpy = d['t_gpy']
		self.t_gpd = d['t_gpd']
		self.t_gph = d['t_gph']
		self.t_gpl = d['t_gpl']
		self.t_rpx = d['t_rpx']
		self.t_rpy = d['t_rpy']
		self.t_rpd = d['t_rpd']
		self.t_rpl = d['t_rpl']
		self.t_sllrx = d['t_sllrx']
		self.t_sllry = d['t_sllry']
		self.t_sllrw = d['t_sllrw']
		self.t_sllrl = d['t_sllrl']
		self.t_sllrh = d['t_sllrh']
		self.t_sludx = d['t_sludx']
		self.t_sludy = d['t_sludy']
		self.t_sludw = d['t_sludw']
		self.t_sludl = d['t_sludl']
		self.t_sludh = d['t_sludh']
		self.t_ppx = d['t_ppx']
		self.t_ppy = d['t_ppy']
		self.t_ppd = d['t_ppd']
		self.t_pph = d['t_pph']
		self.t_pbx = d['t_pbx']
		self.t_pby = d['t_pby']
		self.t_pbw = d['t_pbw']
		self.t_pbl = d['t_pbl']
		self.t_pbh = d['t_pbh']
		self.f_gpx = d['f_gpx']
		self.f_gpy = d['f_gpy']
		self.f_gpd = d['f_gpd']
		self.f_gph = d['f_gph']
		self.f_gpl = d['f_gpl']
		self.f_spx = d['f_spx']
		self.f_spy = d['f_spy']
		self.f_spd = d['f_spd']
		self.f_spd2 = d['f_spd2']
		self.f_spd3 = d['f_spd3']
		self.f_sph = d['f_sph']
		self.f_sph2 = d['f_sph2']
		self.f_sph3 = d['f_sph3']
		self.f_prx = d['f_prx']
		self.f_pry = d['f_pry']
		self.f_prd = d['f_prd']
		self.f_prd2 = d['f_prd2']
		self.f_prh = d['f_prh']
		self.f_prh2 = d['f_prh2']
		self.f_ppx = d['f_ppx']
		self.f_ppy = d['f_ppy']
		self.f_ppd = d['f_ppd']
		self.f_pph = d['f_pph']
		self.f_pbx = d['f_pbx']
		self.f_pby = d['f_pby']
		self.f_pbw = d['f_pbw']
		self.f_pbl = d['f_pbl']
		self.f_pbh = d['f_pbh']
		self.f_aglrx = d['f_aglrx']
		self.f_aglry = d['f_aglry']
		self.f_aglrd = d['f_aglrd']
		self.f_aglrh = d['f_aglrh']
		self.f_aglra = d['f_aglra']
		self.f_aglrl = d['f_aglrl']
		self.f_agudx = d['f_agudx']
		self.f_agudy = d['f_agudy']
		self.f_agudd = d['f_agudd']
		self.f_agudh = d['f_agudh']
		self.f_aguda = d['f_aguda']
		self.f_agudl = d['f_agudl']
		self.order_number = d['order_number']
		self.save_path = s['save_path']
		self.file_type = s['file_type']

	def create_doc(self):
		return FreeCAD.newDocument()

	def read_dimentions(self):
		try:
			res = sql_get_dict(table_name='dimentions')
		except:
			res = {}
			print('Database error.')

		for dimention in res:
			try:
				if dimention in ['t1', 't2', 't3']:
					new = []
					for dim in res[dimention].split(','):
						new.append(float(dim))
					res[dimention] = new
				else:
					res[dimention] = float(res[dimention])
			except:
				print('Can not float: {} = {}'.format(dimention, res[dimention]))
		try:
			if res['w2'] == '':
				res['w2'] = res['w1']
			if res['h2'] == '':
				res['h2'] = res['h1']
		except:
			print('No w1, h1 data')

		try:
			order_number = int(res['order_number'])  # Ex: 10000 > sql 10000.0 > int 10000
			res['order_number'] = order_number
		except:
			pass

		return res


	def read_settings(self):
		res = sql_get_dict(table_name='settings')
		try:
			new_save_path = res['save_path'] + '/'
			res['save_path'] = new_save_path
			return res
		except:
			print('保存先確認')
		try:
			res['file_type']
		except:
			print('Can not get file type, set default is: step')
			res['file_type'] = 'step'


	##### Draw Transfer Molding #####
	def t_draw_plate(self):

		for i in range(len(self.t1)):
			##### Draw main plate #####
			name = 'Transfer_plate_' + str(i)
			if i > 0:
				z = 0
				for j in range(i):
					z += self.t1[j]
			else:
				z = 0

			if i < len(self.t1)-2: # from PL to EJ plate
				Box(self.doc, name, self.w1, self.h1, self.t1[i], 0, 0, z).create_box()

			elif i == len(self.t1)-1: # Base plate
				Box(self.doc, name, self.w2, self.h2, self.t1[i], 0, 0, z).create_box()

			##### Draw EJ plate, EJ space plate #####
			else:

				if self.w3 == '' and self.h3 == '': # EJ plate  データのない場合
					Box(self.doc, name, self.w1, self.h1, self.t1[i], 0, 0, z).create_box()

				elif self.h3 != '': # EJ plate 横型の場合
					# Space plate
					Box(self.doc, name+'_1', self.w1, (self.h1-self.h3)/2-2, self.t1[i], 0, (self.h1+self.h3)/4+1, z).create_box()
					Box(self.doc, name+'_2', self.w1, (self.h1-self.h3)/2-2, self.t1[i], 0, -(self.h1+self.h3)/4-1, z).create_box()

					# EJ plate
					for k in range(len(self.t3)): 
						name_ej = 'Transfer_ej_plate_' + str(k)
						z_ej = z + self.t1[i] - sum(self.t3)
						for j in range(k):
							z_ej += self.t3[j]
						Box(self.doc, name_ej, self.w1, self.h3, self.t3[k], 0, 0, z_ej).create_box()

				elif self.w3 != '': # EJ plate 立型の場合
					# Space plate
					Box(self.doc, name+'_1', (self.w1-self.w3)/2-2, self.h1, self.t1[i], (self.w1+self.w3)/4+1, 0, z).create_box()
					Box(self.doc, name+'_2', (self.w1-self.w3)/2-2, self.h1, self.t1[i], -(self.w1+self.w3)/4-1, 0, z).create_box()

					# EJ plate
					for k in range(len(self.t3)): 
						name_ej = 'Transfer_ej_plate_' + str(k)
						z_ej = z + self.t1[i] - sum(self.t3)
						for j in range(k):
							z_ej += self.t3[j]
						Box(self.doc, name_ej, self.w3, self.h1, self.t3[k], 0, 0, z_ej).create_box()

	def t_draw_slide_core_left_right(self):

		print(self.doc, 'Transfer_slide_core_lr_1', self.t_sllrw, self.t_sllrl, self.t_sllrh,
			self.t_sllrx+self.t_sllrw/2, self.t_sllry, -self.t_sllrh)
		Box(self.doc, 'Transfer_slide_core_lr_1', self.t_sllrw, self.t_sllrl, self.t_sllrh, 
			self.t_sllrx+self.t_sllrw/2, self.t_sllry, -self.t_sllrh).create_box()
		Box(self.doc, 'Transfer_slide_core_lr_2', self.t_sllrw, self.t_sllrl, self.t_sllrh,
			-self.t_sllrx - self.t_sllrw / 2, self.t_sllry, -self.t_sllrh).create_box()
		Box(self.doc, 'Transfer_slide_core_lr_3', self.t_sllrw, self.t_sllrl, self.t_sllrh,
			self.t_sllrx+self.t_sllrw/2, -self.t_sllry, -self.t_sllrh).create_box()
		Box(self.doc, 'Transfer_slide_core_lr_4', self.t_sllrw, self.t_sllrl, self.t_sllrh,
			-self.t_sllrx - self.t_sllrw / 2, -self.t_sllry, -self.t_sllrh).create_box()

	def t_draw_slide_core_up_down(self):
		Box(self.doc, 'Transfer_slide_core_ud_1', self.t_sludl, self.t_sludw, self.t_sludh,
			self.t_sludx, self.t_sludy+self.t_sludw/2, -self.t_sludh).create_box()
		Box(self.doc, 'Transfer_slide_core_ud_2', self.t_sludl, self.t_sludw, self.t_sludh,
			self.t_sludx, -self.t_sludy- self.t_sludw/2, -self.t_sludh).create_box()
		Box(self.doc, 'Transfer_slide_core_ud_3', self.t_sludl, self.t_sludw, self.t_sludh,
			-self.t_sludx, self.t_sludy+self.t_sludw/2, -self.t_sludh).create_box()
		Box(self.doc, 'Transfer_slide_core_ud_4', self.t_sludl, self.t_sludw, self.t_sludh,
			-self.t_sludx, -self.t_sludy- self.t_sludw/2, -self.t_sludh).create_box()

	def t_draw_gp_pin(self):

		if self.t_gpl == '': # lはない場合、plate_0面まで描く
			t_gpl = self.t_gph + self.t1[0]
		else:
			t_gpl = self.t_gpl
		Cylinder(self.doc, 'Transfer_gp1_1', self.t_gpd, t_gpl, self.t_gpx, -self.t_gpy, -self.t_gph).create_cylinder()
		Cylinder(self.doc, 'Transfer_gp1_2', self.t_gpd, t_gpl, self.t_gpx, self.t_gpy, -self.t_gph).create_cylinder()
		Cylinder(self.doc, 'Transfer_gp1_3', self.t_gpd, t_gpl, -self.t_gpx, self.t_gpy, -self.t_gph).create_cylinder()
		Cylinder(self.doc, 'Transfer_gp1_4', self.t_gpd, t_gpl, -self.t_gpx, -self.t_gpy, -self.t_gph).create_cylinder()

	def t_draw_rp_pin(self):

		if self.t_rpl == '':
			if self.t3 == '':
				t_rpl = sum(self.t1) # RPの長さはない場合、金型厚み分で作成
			else:
				t_rpl = sum(self.t1) - self.t1[-1] - self.t3[-1]
		else:
			t_rpl = self.t_rpl
		Cylinder(self.doc, 'Transfer_ej1_1', self.t_rpd, t_rpl, self.t_rpx, self.t_rpy, 0).create_cylinder()
		Cylinder(self.doc, 'Transfer_ej1_2', self.t_rpd, t_rpl, self.t_rpx, -self.t_rpy, 0).create_cylinder()
		Cylinder(self.doc, 'Transfer_ej1_3', self.t_rpd, t_rpl, -self.t_rpx, self.t_rpy, 0).create_cylinder()
		Cylinder(self.doc, 'Transfer_ej1_4', self.t_rpd, t_rpl, -self.t_rpx, -self.t_rpy, 0).create_cylinder()

	def t_draw_pp_pin(self): # Position pin
		Cylinder(self.doc, 'Transfer_pp1_1', self.t_ppd, self.t_pph, self.t_ppx, self.t_ppy, -self.t_pph).create_cylinder()
		Cylinder(self.doc, 'Transfer_pp1_2', self.t_ppd, self.t_pph, self.t_ppx, -self.t_ppy, -self.t_pph).create_cylinder()
		Cylinder(self.doc, 'Transfer_pp1_3', self.t_ppd, self.t_pph, -self.t_ppx, self.t_ppy, -self.t_pph).create_cylinder()
		Cylinder(self.doc, 'Transfer_pp1_4', self.t_ppd, self.t_pph, -self.t_ppx, -self.t_ppy, -self.t_pph).create_cylinder()

	def t_draw_pb_block(self):  # Position block
		Box(self.doc, 'Transfer_pos_block_1', self.t_pbw, self.t_pbl, self.t_pbh,
			self.t_pbx, self.t_pby, -self.t_pbh).create_box()
		Box(self.doc, 'Transfer_pos_block_2', self.t_pbw, self.t_pbl, self.t_pbh,
			-self.t_pbx, -self.t_pby, -self.t_pbh).create_box()

	##### Draw Fixed Molding #####
	def f_draw_plate(self):
		for i in range(len(self.t2)):
			##### Draw main plate #####
			name = 'Fixed_plate_' + str(i)
			if i > 0:
				z = -self.t2[0]
				for j in range(1,i+1):
					z -= self.t2[j]
			else:
				z = -self.t2[0]
			if i < len(self.t2)-1:
				Box(self.doc, name, self.w1, self.h1, self.t2[i], 0, 0, z).create_box()
			elif i == len(self.t2)-1: # Base plate
				Box(self.doc, name, self.w2, self.h2, self.t2[i], 0, 0, z).create_box()

	def f_draw_gp_pin(self):
		if self.f_gpl == '': # lはない場合、plate_0面まで描く
			try:
				f_gpl = self.f_gph + self.t2[0]
				z_gp1 = - self.t2[0]
			except:
				f_gpl = self.f_gph + 30 # 固定型の厚みはない場合、仮 t2[0] = 30mm
				z_gp1 = - 30 # 固定型の厚みはない場合、仮 t2[0] = 30mm
		else:
			f_gpl = self.f_gpl
			z_gp1 = -f_gpl + self.f_gph
		Cylinder(self.doc, 'Fixed_gp1_1', self.f_gpd, f_gpl, self.f_gpx, self.f_gpy, z_gp1).create_cylinder()
		Cylinder(self.doc, 'Fixed_gp1_2', self.f_gpd, f_gpl, self.f_gpx, -self.f_gpy, z_gp1).create_cylinder()
		Cylinder(self.doc, 'Fixed_gp1_3', self.f_gpd, f_gpl, -self.f_gpx, self.f_gpy, z_gp1).create_cylinder()
		Cylinder(self.doc, 'Fixed_gp1_4', self.f_gpd, f_gpl, -self.f_gpx, -self.f_gpy, z_gp1).create_cylinder()

	def f_draw_sp_pin(self):

		if self.f_spd2 == '':
			self.f_spd2 = self.f_spd
		if self.f_spd3 == '':
			self.f_spd3 = self.f_spd	
		if self.f_sph2 == '':
			self.f_sph2 = 0.01
		if self.f_sph3 == '':
			self.f_sph3 = 0.01

		sp1_l = self.f_sph - self.f_sph2 - self.f_sph3 + sum(self.t2)
		sp1_z = -sum(self.t2)

		l1 = [1, 1, -1, -1]
		l2 = [1, -1, 1, -1]
		sp_obj = [] # SP pin obj list
		for i in range(4):
			sp_obj.append('Fixed_sp1_' + str(i+1))
			sp_obj_child = ['_sp1_'+str(i+1)+'_1', '_sp1_'+str(i+1)+'_2', '_sp1_'+str(i+1)+'_3']

			# Creat parts of SP pin
			sp_obj_child[0] = Cylinder(self.doc, '_sp1_'+str(i+1)+'_1', self.f_spd, sp1_l,
									   self.f_spx*l1[i], self.f_spy*l2[i], sp1_z).create_cylinder(), # Pin
			sp_obj_child[1] = Cylinder(self.doc, '_sp1_'+str(i+1)+'_2', self.f_spd2, self.f_sph2,
									   self.f_spx*l1[i], self.f_spy*l2[i], sp1_z+sp1_l).create_cylinder(), # カラー
			sp_obj_child[2] = Cylinder(self.doc, '_sp1_'+str(i+1)+'_3', self.f_spd3, self.f_sph3,
									   self.f_spx*l1[i], self.f_spy*l2[i], sp1_z+sp1_l+self.f_sph2).create_cylinder() # Head

			# Add child part into SP pin
			sp_obj[i] = self.doc.addObject("Part::MultiFuse",'Fixed_sp1_' + str(i+1))
			sp_obj[i].Shapes = [self.doc.getObject('_sp1_'+str(i+1)+'_1'), 
							self.doc.getObject('_sp1_'+str(i+1)+'_2'), 
							self.doc.getObject('_sp1_'+str(i+1)+'_3')]

	def f_draw_pr_pin(self):

		if self.f_prd2 == '':
			self.f_prd2 = self.f_prd
		if self.f_prh2 == '':
			self.f_prh2 = self.f_prh

		pr1_l = self.f_prh - self.f_prh2 + sum(self.t2) - self.t2[-1] - self.t2[-2]
		pr1_z = -( sum(self.t2) - self.t2[-1] - self.t2[-2] )

		l1 = [1, 1, -1, -1]
		l2 = [1, -1, 1, -1]
		pr_obj = []
		for i in range(4):
			pr_obj.append('Fixed_pr1_' + str(i+1))
			pr_obj_child = ['_pr1_'+str(i+1)+'_1', '_pr1_'+str(i+1)+'_2', '_pr1_'+str(i+1)+'_3']

			# Creat parts of PR bolt
			pr_obj_child[0] = Cylinder(self.doc, '_pr1_'+str(i+1)+'_1', self.f_prd, pr1_l, self.f_prx*l1[i], self.f_pry*l2[i], pr1_z).create_cylinder(), # Pin
			pr_obj_child[0] = Cylinder(self.doc, '_pr1_'+str(i+1)+'_2', self.f_prd2, self.f_prh2, self.f_prx*l1[i], self.f_pry*l2[i], pr1_z+pr1_l).create_cylinder(), # Pin

			# Add child part into PR pin
			pr_obj[i] = self.doc.addObject("Part::MultiFuse",'Fixed_pr1_' + str(i+1))
			pr_obj[i].Shapes = [self.doc.getObject('_pr1_'+str(i+1)+'_1'), 
							self.doc.getObject('_pr1_'+str(i+1)+'_2')]

	def f_draw_pp_pin(self): # Position pin
		Cylinder(self.doc, 'Fixed_pp1_1', self.f_ppd, self.f_pph, self.f_ppx, self.f_ppy, 0).create_cylinder()
		Cylinder(self.doc, 'Fixed_pp1_2', self.f_ppd, self.f_pph, self.f_ppx, -self.f_ppy, 0).create_cylinder()
		Cylinder(self.doc, 'Fixed_pp1_3', self.f_ppd, self.f_pph, -self.f_ppx, self.f_ppy, 0).create_cylinder()
		Cylinder(self.doc, 'Fixed_pp1_4', self.f_ppd, self.f_pph, -self.f_ppx, -self.f_ppy, 0).create_cylinder()

	def f_draw_pb_block(self):  # Position block
		Box(self.doc, 'Fixed_pos_block_1', self.f_pbw, self.f_pbl, self.f_pbh,
			self.f_pbx, self.f_pby, 0).create_box()
		Box(self.doc, 'Fixed_pos_block_2', self.f_pbw, self.f_pbl, self.f_pbh,
			-self.f_pbx, -self.f_pby, 0).create_box()

	def f_draw_angular_pin_lr(self):
		if self.f_aglrl == '':
			f_aglrl = self.f_aglrh / math.cos(math.radians(self.f_aglra)) + 20 # Defaut upto PL + 20mm
		else:
			f_aglrl = self.f_aglrl
		# # Left right angular pin
		AngularCylinder(self.doc, 'Fixed_ag_lr_1',
			self.f_aglrd, f_aglrl, self.f_aglrh, self.f_aglrx, self.f_aglry, 0, 
			0, self.f_aglra, 0).create_angular_pin()
		AngularCylinder(self.doc, 'Fixed_ag_lr_2',
			self.f_aglrd, f_aglrl, self.f_aglrh, -self.f_aglrx, self.f_aglry, 0,
			0, -self.f_aglra, 0).create_angular_pin()
		AngularCylinder(self.doc, 'Fixed_ag_lr_3',
			self.f_aglrd, f_aglrl, self.f_aglrh, self.f_aglrx, -self.f_aglry, 0,
			0, self.f_aglra, 0).create_angular_pin()
		AngularCylinder(self.doc, 'Fixed_ag_lr_4',
			self.f_aglrd, f_aglrl, self.f_aglrh, -self.f_aglrx, -self.f_aglry, 0,
			0, -self.f_aglra, 0).create_angular_pin()

	def f_draw_angular_pin_ud(self):
		if self.f_agudl == '':
			f_agudl = self.f_agudh / math.cos(math.radians(self.f_aguda)) + 20 # # Defaut upto PL + 20mm
		else:
			f_agudl = self.f_agudl
		AngularCylinder(self.doc, 'Fixed_ag_ud_1',
			self.f_agudd, f_agudl, self.f_agudh, self.f_agudx, self.f_agudy, 0,
			0, 0, -self.f_aguda).create_angular_pin()
		AngularCylinder(self.doc, 'Fixed_ag_ud_2',
			self.f_agudd, f_agudl, self.f_agudh, -self.f_agudx, self.f_agudy, 0,
			0, 0, -self.f_aguda).create_angular_pin()
		AngularCylinder(self.doc, 'Fixed_ag_ud_3',
			self.f_agudd, f_agudl, self.f_agudh, self.f_agudx, -self.f_agudy, 0,
			0, 0, self.f_aguda).create_angular_pin()
		AngularCylinder(self.doc, 'Fixed_ag_ud_4',
			self.f_agudd, f_agudl, self.f_agudh, -self.f_agudx, -self.f_agudy, 0,
			0, 0, self.f_aguda).create_angular_pin()

	def f_draw_nozzle(self):
		Cylinder(self.doc, 'Fixed_nozzle', 100, 10, 0, 0, -sum(self.t2) - 10).create_cylinder() # 仮寸法

	##### Move Object ##### obj_name: a part of name ok
	def move_obj(self, obj_name, x, y, z):
		for obj in self.doc.Objects:
			if obj_name in obj.Name:
				old_vec = obj.Placement.Base
				move_vec = FreeCAD.Vector(x, y, z)
				obj.Placement.Base = old_vec + move_vec

	##### Main Draw Molding #####
	def main_drawing_molding(self):
		note = []
		error = []

		# Transfer main plate
		try:
			if '' not in [self.w1, self.h1, self.t1]:
				self.t_draw_plate()
			else:
				note.append('移動型_プレート')
		except:
			error.append('移動型_プレート')

		# Transfer GP
		try:
			if '' not in [self.t_gpx, self.t_gpy, self.t_gpd, self.t_gph]:
				self.t_draw_gp_pin()
			else:
				note.append('移動型_GP')
		except:
			error.append('移動型_GP')

		# Transfer RP
		try:
			if '' not in [self.t_rpx, self.t_rpy, self.t_rpd]:
					self.t_draw_rp_pin()
			else:
				note.append('移動型_RP')
		except:
			error.append('移動型_RP')

		# Transfer Slide core left right
		try:
			if '' not in [self.t_sllrx, self.t_sllry, self.t_sllrw, self.t_sllrl, self.t_sllrh]:
					self.t_draw_slide_core_left_right()
			else:
				note.append('移動型_スライドコア・左右')
		except:
			error.append('移動型_スライドコア・左右')

		# Transfer Slide core up down
		try:
			if '' not in [self.t_sludx, self.t_sludy, self.t_sludw, self.t_sludl, self.t_sludh]:
				self.t_draw_slide_core_up_down()
			else:
				note.append('移動型_スライドコア・上下')
		except:
			error.append('移動型_スライドコア・上下')

		# Transfer pp pin
		try:
			if '' not in [self.t_ppx, self.t_ppy, self.t_ppd, self.t_pph]:
				self.t_draw_pp_pin()
			else:
				note.append('移動型_テーパピン')
		except:
			error.append('移動型_テーパピン')

		# Transfer pp block
		try:
			if '' not in [self.t_pbx, self.t_pby, self.t_pbw, self.t_pbl, self.t_pbh]:
				self.t_draw_pb_block()
			else:
				note.append('移動型_テーパブロック')
		except:
			error.append('移動型_テーパブロック')

		# Fixed main plate and nozzle
		try:
			if '' not in [self.w1, self.h1, self.t2]:
				self.f_draw_plate()
				self.f_draw_nozzle()
			else:
				note.append('固定型_プレート')
		except:
			error.append('固定型_プレート')

		# Fixed GP
		try:
			if '' not in [self.f_gpx, self.f_gpy, self.f_gpd, self.f_gph]:
				self.f_draw_gp_pin()
			else:
				note.append('固定型_GP')
		except:
			error.append('固定型_GP')

		# Fixed SP
		try:
			if '' not in [self.f_spx, self.f_spy, self.f_spd, self.f_sph]:
				self.f_draw_sp_pin()
			else:
				note.append('固定型_SP')
		except:
			error.append('固定型_SP')

		# Fixed PR
		try:
			if '' not in [self.f_prx, self.f_pry, self.f_prd, self.f_prh]:
				self.f_draw_pr_pin()
			else:
				note.append('固定型_プラボルト')
		except:
			error.append('固定型_プラボルト')

		# Fixed pp pin
		try:
			if '' not in [self.f_ppx, self.f_ppy, self.f_ppd, self.f_pph]:
				self.f_draw_pp_pin()
			else:
				note.append('固定型_テーパピン')
		except:
			error.append('固定型_テーパピン')

		# Fixed pp block
		try:
			if '' not in [self.f_pbx, self.f_pby, self.f_pbw, self.f_pbl, self.f_pbh]:
				self.f_draw_pb_block()
			else:
				note.append('固定型_テーパブロック')
		except:
			error.append('固定型_テーパブロック')

		# Fixed angular pin
		try:
			if '' not in [self.f_aglrx, self.f_aglry, self.f_aglrd, self.f_aglrh, self.f_aglra]:
				self.f_draw_angular_pin_lr()
			else:
				note.append('固定型_アンギュラピン・左右')
		except:
			error.append('固定型_アンギュラピン・左右')

		# Fixed angular pin
		try:
			if '' not in [self.f_agudx, self.f_agudy, self.f_agudd, self.f_agudh, self.f_aguda]:
				self.f_draw_angular_pin_ud()
			else:
				note.append('固定型_アンギュラピン・上下')
		except:
			error.append('固定型_アンギュラピン・上下')

		return {'note':note, 'error':error}

		##### Main Open Molding #####
	def open_mold(self):
		try:
			self.move_obj('Transfer_ej', 0, 0, -self.ej) # Open EJ
		except:
			print('Can not open EJ, EJ = %s' % self.ej)

		try:
			self.move_obj('Fixed', 0, 0, -self.o1) # Open product side
		except:
			print('Can not open product side, Open = %s' % self.ej)
		try:
			open_nozzle = [	'Fixed_plate_' + str(len(self.t2)-1), 'Fixed_sp1', 'Fixed_nozzle']
			for name in open_nozzle:
				self.move_obj(name, 0, 0, -self.o3) # Open nozzle side
		except:
			print('Can not open nozzle side, Open = %s' % self.ej)
		try:
			open_nozzle = ['Fixed_plate_' + str(len(self.t2) - 1), 'Fixed_sp1', 'Fixed_nozzle']
			open_runner = open_nozzle + ['Fixed_plate_' + str(len(self.t2)-2), 'Fixed_pr1']
			for name in open_runner:
				self.move_obj(name, 0, 0, -self.o2) # Open runner side	
		except:
			print('Can not open runner side, Open = %s' % self.ej)

	############## Export file all object #############################
	def export_file(self):
		# Read database:
		if self.file_type == 'FCStd':
			self.doc.recompute()  # Alway recomputer before save file
			self.doc.saveAs(u"{}Mold_{}.FCStd".format(self.save_path, self.order_number))
		else:
			self.doc.recompute()
			select = []
			for obj in self.doc.Objects:
				if obj.Name[:5] in ['Trans', 'Fixed']:
					select.append(obj)
			self.doc.recompute()
			Import.export(select, "{}Mold_{}.{}".format(self.save_path, self.order_number, self.file_type))

# Save error to csv file in database forder can use when built app
def _save_note_error(note_error):
	# Get database path
	now_path = os.path.dirname(os.path.abspath(__file__))
	parent_dir = Path(now_path).parent.parent.joinpath('database') # Database Dir
	path = str(parent_dir).replace('\\', '/') + '/note_and_error.csv'
	# path = 'C:/Users/DELL/Desktop/t13/database/note_and_error.csv'
	# print(path)
	row_list = [['作成しない', 'エラー']]
	for i in range(max(len(note_error['note']), len(note_error['error']))):
		row = []
		try:
			col_1 = note_error['note'][i]
		except:
			col_1 = ''
		try:
			col_2 = note_error['error'][i]
		except:
			col_2 = ''
		row_list.append([col_1, col_2])
	try:
		with open(path, 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerows(row_list)
	except:
		pass

# Main
def _main_drawing():
	molding = Molding()
	note_error = molding.main_drawing_molding()
	molding.open_mold()
	molding.export_file()
	_save_note_error(note_error)
	print(note_error)

#################################################################
if __name__ == '__main__':
	_main_drawing()
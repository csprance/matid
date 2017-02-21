import modo

from colours import Color


class MatIDApplyClass(object):
	def __init__(self, rgbstring):
		super(MatIDApplyClass)
		self.swatch_color_string = rgbstring
		self.swatch_rgb = Color(rgb=self.split_string_to_rgb(self.swatch_color_string))
		self.scene = modo.Scene()
		self.mesh = modo.Mesh()
		self.selected_polys = self.mesh.geometry.polygons.selected

	def create_material(self):
		# if the material exists don't create it use it instead
		if '%s' % self.swatch_rgb not in [x.name for x in self.scene.items('mask')]:
			print 'Creating non existent swatch material'
			# We will assign the material per polygon, so we need to use a mask item
			mask = self.scene.addItem('mask', name='%s' % self.swatch_rgb)

			# Create a new material with a blue diffuse color
			mat = self.scene.addMaterial()
			mat.channel('diffCol').set(self.swatch_rgb.rgb)
			mat.channel('diffAmt').set(1)

			# Tell the mask to use our material
			mask.channel('ptag').set(self.swatch_color_string)

			# Parent the material to the mask
			mat.setParent(mask, index=1)

			# This places the mask item below the base shader in the hierarchy of the Shader Tree
			mask.setParent(self.scene.renderItem, index=1)

		# Assign the material to the selected polygons
		with self.mesh.geometry as obj:
			for poly in obj.polygons.selected:
				poly.materialTag = self.swatch_color_string

	@staticmethod
	def split_string_to_rgb(string_to_split):
		return float(string_to_split[0:3]), float(string_to_split[3:6]), float(string_to_split[6:9])

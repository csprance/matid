import lx
import lxifc
import lxu.command
import modo


class MatIDApplyClass(object):
    def __init__(self, rgbstring):
        super(MatIDApplyClass)
        self.swatch_color_string = rgbstring
        self.swatch_rgb = self.split_string_to_rgb(self.swatch_color_string)
        self.scene = modo.Scene()
        self.mesh = modo.Mesh()
        self.selected_polys = self.mesh.geometry.polygons.selected

    def create_material(self):
        self.swatch_rgb = self.split_string_to_rgb(self.swatch_color_string)
        # We will assign the material per polygon, so we need to use a mask item
        mask = self.scene.addItem('mask', name=self.swatch_color_string)

        # Create a new material with a blue diffuse color
        mat = self.scene.addMaterial()
        mat.channel('diffCol').set(self.swatch_rgb)

        # Tell the mask to use our material
        mask.channel('ptag').set(self.swatch_color_string)

        # Parent the material to the mask
        mat.setParent(mask, index=1)

        # This places the mask item below the base shader in the hierarchy of the Shader Tree
        mask.setParent(self.scene.renderItem, index=1)

        # Assign the material the selected polygons
        for poly in self.selected_polys:
            print poly
            # poly.materialTag = self.swatch_color_string

        # Update the mesh to see the result
        self.mesh.geometry.setMeshEdits()

    def split_string_to_rgb(self, string_to_split):
        return (float(string_to_split[0:3]),
                float(string_to_split[3:6]),
                float(string_to_split[6:9]))

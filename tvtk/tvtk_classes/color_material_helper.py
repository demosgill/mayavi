# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.object import Object


class ColorMaterialHelper(Object):
    """
    ColorMaterialHelper - a helper to assist in simulating the
    
    Superclass: Object
    
    ColorMaterialHelper is a helper to assist in simulating the
     color_material behaviour of the default open_gl pipeline. Look at
     ColorMaterialHelper_s for available GLSL functions.
    
    See Also:
    
    
     ShaderProgram2
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkColorMaterialHelper, obj, update, **traits)
    
    def _get_shader(self):
        return wrap_vtk(self._vtk_obj.GetShader())
    shader = traits.Property(_get_shader, help=\
        """
        
        """
    )

    def initialize(self, *args):
        """
        V.initialize(ShaderProgram2)
        C++: void Initialize(ShaderProgram2 *)"""
        my_args = [deref_vtk(x) for x in args]
        ret = self._wrap_call(self._vtk_obj.Initialize, *my_args)
        return ret

    def prepare_for_rendering(self):
        """
        V.prepare_for_rendering()
        C++: void PrepareForRendering()
        Prepares the shader i.e. reads color material paramters state
        from open_gl. This must be called before the shader is bound.
        """
        ret = self._vtk_obj.PrepareForRendering()
        return ret
        

    def render(self):
        """
        V.render()
        C++: void Render()
        Uploads any uniforms needed. This must be called only after the
        shader has been bound, but before rendering the geometry.
        """
        ret = self._vtk_obj.Render()
        return ret
        

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ColorMaterialHelper, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ColorMaterialHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit ColorMaterialHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ColorMaterialHelper properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

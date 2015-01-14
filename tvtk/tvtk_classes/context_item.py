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

from tvtk.tvtk_classes.abstract_context_item import AbstractContextItem


class ContextItem(AbstractContextItem):
    """
    ContextItem - base class for items that are part of a
    ContextScene.
    
    Superclass: AbstractContextItem
    
    Derive from this class to create custom items that can be added to a
    ContextScene.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkContextItem, obj, update, **traits)
    
    opacity = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set the opacity of the item. 1.0 by default.
        """
    )
    def _opacity_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetOpacity,
                        self.opacity)

    _updateable_traits_ = \
    (('opacity', 'GetOpacity'), ('reference_count', 'GetReferenceCount'),
    ('global_warning_display', 'GetGlobalWarningDisplay'), ('debug',
    'GetDebug'), ('visible', 'GetVisible'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display', 'opacity', 'visible'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ContextItem, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], ['opacity', 'visible']),
            title='Edit ContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ContextItem properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

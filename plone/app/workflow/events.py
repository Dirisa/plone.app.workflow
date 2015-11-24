from zope.interface import classImplements, implementer
from zope.lifecycleevent import ObjectModifiedEvent
from plone.app.workflow.interfaces import ILocalrolesModifiedEvent

#@implementer(ILocalrolesModifiedEvent)
class LocalrolesModifiedEvent(ObjectModifiedEvent):
    pass
classImplements(LocalrolesModifiedEvent, ILocalrolesModifiedEvent)

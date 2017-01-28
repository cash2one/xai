

#calss header
class _FOREIGN():
	def __init__(self,): 
		self.name = "FOREIGN"
		self.definitions = [u'belonging or connected to a country that is not your own: ', u'Something can be described as foreign to a particular person if they do not know about it or it is not within their experience: ', u'A foreign object or substance has entered something else, possibly by accident, and does not belong there: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

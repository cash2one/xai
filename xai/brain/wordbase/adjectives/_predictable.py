

#calss header
class _PREDICTABLE():
	def __init__(self,): 
		self.name = "PREDICTABLE"
		self.definitions = [u'Something that is predictable happens in a way or at a time that you know about before it happens: ', u'happening or behaving in a way that you expect and not unusual or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

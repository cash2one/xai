

#calss header
class _INCURABLE():
	def __init__(self,): 
		self.name = "INCURABLE"
		self.definitions = [u'not able to be cured: ', u"used to say that someone 's personality type does not change or cannot be changed: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

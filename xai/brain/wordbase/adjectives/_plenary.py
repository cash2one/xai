

#calss header
class _PLENARY():
	def __init__(self,): 
		self.name = "PLENARY"
		self.definitions = [u'A plenary meeting is one at which all the members of a group or organization are present, especially at a conference: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

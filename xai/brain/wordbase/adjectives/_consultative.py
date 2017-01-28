

#calss header
class _CONSULTATIVE():
	def __init__(self,): 
		self.name = "CONSULTATIVE"
		self.definitions = [u'A consultative group or document gives advice about something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

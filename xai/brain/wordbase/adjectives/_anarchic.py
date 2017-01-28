

#calss header
class _ANARCHIC():
	def __init__(self,): 
		self.name = "ANARCHIC"
		self.definitions = [u'not showing respect for official or accepted rules, behaviour, organizations, leaders, etc.: ', u'without organization or control, especially describing a society with no government or a very weak government']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

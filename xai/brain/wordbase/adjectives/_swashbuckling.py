

#calss header
class _SWASHBUCKLING():
	def __init__(self,): 
		self.name = "SWASHBUCKLING"
		self.definitions = [u'behaving in a brave and exciting way, especially like a fighter in the past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _GRIEVING():
	def __init__(self,): 
		self.name = "GRIEVING"
		self.definitions = [u'feeling very sad because someone has died: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

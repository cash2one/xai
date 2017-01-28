

#calss header
class _HUMANE():
	def __init__(self,): 
		self.name = "HUMANE"
		self.definitions = [u'showing kindness, care, and sympathy towards others, especially those who are suffering: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata



#calss header
class _SICKENING():
	def __init__(self,): 
		self.name = "SICKENING"
		self.definitions = [u'extremely unpleasant and causing you to feel shock and anger: ', u'annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

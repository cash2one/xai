

#calss header
class _MAUDLIN():
	def __init__(self,): 
		self.name = "MAUDLIN"
		self.definitions = [u'feeling sad and sorry for yourself, especially after you have drunk a lot of alcohol']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

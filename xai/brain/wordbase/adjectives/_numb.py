

#calss header
class _NUMB():
	def __init__(self,): 
		self.name = "NUMB"
		self.definitions = [u'If a part of your body is numb, you are unable to feel it, usually for a short time: ', u'not able to feel any emotions or to think clearly, because you are so shocked or frightened, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

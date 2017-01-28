

#calss header
class _BLINKERED():
	def __init__(self,): 
		self.name = "BLINKERED"
		self.definitions = [u"A blinkered person is unable or unwilling to understand other people's beliefs, and blinkered opinions or ways of behaving show someone is unable or unwilling to understand other people: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

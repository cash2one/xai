

#calss header
class _GYNAECOLOGICAL():
	def __init__(self,): 
		self.name = "GYNAECOLOGICAL"
		self.definitions = [u"relating to gynaecology (= the area of medicine concerned with disorders and functions of women's reproductive organs): "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

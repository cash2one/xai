

#calss header
class _SULTRY():
	def __init__(self,): 
		self.name = "SULTRY"
		self.definitions = [u'(of weather) uncomfortably warm and with air that is slightly wet', u"(especially of a woman's face or voice) attractive in a way that suggests sexual desire: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

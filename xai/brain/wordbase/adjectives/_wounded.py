

#calss header
class _WOUNDED():
	def __init__(self,): 
		self.name = "WOUNDED"
		self.definitions = [u'offended or upset by what someone has said or done: ', u'injured, especially with a cut or hole in the skin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

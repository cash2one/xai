

#calss header
class _DESIGNATE():
	def __init__(self,): 
		self.name = "DESIGNATE"
		self.definitions = [u'used after the title of a particular official job to refer to someone chosen to do that job, but who has not yet started doing it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

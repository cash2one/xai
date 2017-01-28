

#calss header
class _LATENT():
	def __init__(self,): 
		self.name = "LATENT"
		self.definitions = [u'present but needing particular conditions to become active, obvious, or completely developed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata

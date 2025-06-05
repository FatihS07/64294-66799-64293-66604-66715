import axios from 'axios';
  
export const fetchGenerateNumbers = async () => {
    return axios.get('/api/generate/')
}
export const fetchStatistics = async () => {
    return axios.get('/api/stats/')
}
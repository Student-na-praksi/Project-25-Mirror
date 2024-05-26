
// src/api.ts
import { LocationResponse } from './types';

export async function fetchPloughLocationsAndWaypoints(id: number): Promise<LocationResponse> {
  const response = await fetch(`http://127.0.0.1:7000/get-locations?id=${id}`);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  const data: LocationResponse = await response.json();
  return data;
}
